#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_level0.py — level-0 正本レコードの machine checks（全スプレッド共通）。

level0_schema.json > validation.machine_checks に準拠する単一の checker。
スプレッド専用 checker（check_f1 〜 check_f8f9）を置き換える。

設計方針（f6-f7 版 checker の共通設計を継承し、f8-f9 版の汎用化を取り込む）:
  * 判定は PASS / FAIL / SKIP の三値。適用対象のない検査、および照合に必要な
    依存ファイルが同梱されていない検査は SKIP とし、合否の母数から除外する。
  * LABELS は正典順の定数。--labels で出力し、schema の machine_checks と
    verify_sync.py により機械的に同期を検証する。
  * 検査対象の面（faces）は spread_id から導出する（ハードコードしない）。
  * cl_global_* の参照検査は構造キー走査で行い、散文中の言及は INFO 扱い。
  * typography_scale.json を要するのは type_class=null の paratext 照合と
    錨照合の2項目のみ。
  * パスはすべて明示引数か __file__ 基準。open() は with 文・encoding="utf-8"。
  * 第3項（2026-11-24 改訂）：face 訂正のあるユニットは、revision_history の face
    エントリが id の面接頭辞から現在の face まで途切れず連鎖することを検査する。
  * 第21項（2026-11-24 追加）：deprecated_ids の旧 id が units に残らず、
    superseded_by（文字列または配列）が現存 id に解決することを検査する。

usage:
    python3 check_level0.py --record f14-f15_level0.json [--refs DIR]
    python3 check_level0.py --all DIR [--refs DIR]     # ディレクトリ内の全正本
    python3 check_level0.py --labels
"""

import argparse
import glob
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

# level0_schema.json > validation.machine_checks と一字一句同一に保つ
LABELS = [
    "全 id が一意",
    "id が tu_ 接頭辞・命名規則に適合",
    "id の面接頭辞が face と一致、または face 訂正の連鎖が接頭辞から現在の face まで途切れない",
    "unit_count == len(units)",
    "seq がスプレッド内で一意",
    "face ∈ spread_id の構成面",
    "type_class が整数 {1,2,3,4} または null",
    "type_class=null のユニットは note と paratext_sizes 錨を持つ",
    "typography_scale.json の錨と type_class が一致",
    "style ∈ {romain, italique, mixte}",
    "style='mixte' のユニットは note 非 null",
    "revision_history の必須キーと field ∈ {text, face}",
    "deprecated_ids の必須キー",
    "text に U+0027 が残存しない",
    "text が NFC 正規化済み",
    "text が非空かつ前後空白なし",
    "構造上参照する cl_global_* が台帳に実在",
    "台帳から当該スプレッドへの未解決参照なし",
    "open_questions が二区分運用に適合",
    "status が既定語彙",
    "deprecated_ids の旧 id が重複せず units に残らず、superseded_by が現存 id に解決する",
]

STYLES = {"romain", "italique", "mixte"}
RH_KEYS = {"date", "unit_id", "field", "before", "after", "evidence", "by"}
DEP_KEYS = {"id", "superseded_by", "date", "evidence", "by"}
STATUS_VOCAB = {"draft_awaiting_collation", "awaiting_collation",
                "awaiting_verbatim_collation", "collated_with_original"}
REF_KEYS = {"clause", "clause_id", "clause_ref", "clause_refs", "clauses",
            "global_clause", "global_clauses", "relations", "relations_in",
            "relations_out", "from", "to", "target"}
CLAUSE_RE = re.compile(r"cl_global_[a-z0-9_]+")
ID_RE = re.compile(r"^tu_(f\d+)_[a-z0-9_]+$")

# open_questions の別名。旧世代のレコードは open_issues を用いる。
OQ_SECTIONS = ("open_questions", "open_issues")


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_scale(path):
    """typography_scale.json から錨を抽出する。

    返り値 (class_anchors, paratext_anchors, recognized)。
      class_anchors    : text_unit -> size_class（size_classes[].anchors 由来）
      paratext_anchors : text_unit の集合（paratext_sizes 附属節由来）
      recognized       : 想定構造を認識できたか

    クラス識別キーは v0.3 本体で "size_class"。旧 update 由来の別名も許容する
    （候補に size_class を含めないと錨が1件も収集されず、錨照合が誤って
     SKIP に落ちる——2026-08-24 に f6-f7 版 checker で検出した不具合）。
    """
    if not path or not os.path.exists(path):
        return {}, set(), False
    scale = load_json(path)

    def unit_of(anchor):
        if not isinstance(anchor, dict):
            return None
        loc = anchor.get("anchor_location")
        if isinstance(loc, dict) and loc.get("text_unit"):
            return loc["text_unit"]
        return anchor.get("text_unit")

    class_anchors, paratext_anchors, recognized = {}, set(), False

    classes = scale.get("size_classes")
    if isinstance(classes, list):
        recognized = True
        for sc in classes:
            if not isinstance(sc, dict):
                continue
            cid = next((sc[k] for k in ("size_class", "class", "class_id", "type_class")
                        if type(sc.get(k)) is int), None)
            for anchor in sc.get("anchors") or []:
                tu = unit_of(anchor)
                if tu and cid is not None:
                    class_anchors[tu] = cid

    annex = scale.get("paratext_sizes")
    if isinstance(annex, dict):
        recognized = True
        for anchor in annex.get("anchors") or []:
            tu = unit_of(anchor)
            if tu:
                paratext_anchors.add(tu)

    return class_anchors, paratext_anchors, recognized


def face_chain_problem(unit, rh):
    """第3項。問題がなければ None、あれば理由の文字列を返す。

    face 訂正なし → id の面接頭辞 == 現在の face。
    face 訂正あり → 記載順の face エントリが連鎖し、始点 before == 接頭辞、
                    終点 after == 現在の face。
    """
    m = ID_RE.match(str(unit.get("id", "")))
    prefix = m.group(1) if m else None
    face = unit.get("face")
    chain = [e for e in rh if e.get("unit_id") == unit.get("id") and e.get("field") == "face"]
    if not chain:
        return None if prefix == face else "接頭辞 %s ≠ face %s（訂正記録なし）" % (prefix, face)
    if chain[0].get("before") != prefix:
        return "最初の訂正の before %s ≠ 接頭辞 %s" % (chain[0].get("before"), prefix)
    for a, b in zip(chain, chain[1:]):
        if a.get("after") != b.get("before"):
            return "訂正の連鎖が途切れる（%s の後に %s）" % (a.get("after"), b.get("before"))
    if chain[-1].get("after") != face:
        return "最後の訂正の after %s ≠ 現在の face %s" % (chain[-1].get("after"), face)
    return None


def deprecation_problems(dep, ids):
    """第21項。旧 id が units に残らず、後継が現存 id に解決するか。"""
    current = set(ids)
    table = {}
    problems = []
    for e in dep:
        sb = e.get("superseded_by")
        if e.get("id") in table:
            # 同じ旧 id の重複登録は後の記載が先の記載を上書きしてしまうため、検出して FAIL とする
            problems.append("%s が deprecated_ids に重複登録" % e.get("id"))
        table[e.get("id")] = sb if isinstance(sb, list) else [sb]

    def resolves(tid, seen):
        if tid in current:
            return True
        if tid in table and tid not in seen:
            return all(resolves(t, seen | {tid}) for t in table[tid])
        return False

    for old, succ in table.items():
        if old in current:
            problems.append("%s が units に残存" % old)
        if not succ or not all(isinstance(t, str) for t in succ):
            problems.append("%s の superseded_by が不正" % old)
        elif not resolves(old, set()):
            problems.append("%s が現存 id に解決しない（%s）" % (old, succ))
    return problems


def walk_strings(node):
    if isinstance(node, dict):
        for v in node.values():
            yield from walk_strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk_strings(v)
    elif isinstance(node, str):
        yield node


def structural_clause_refs(node, key=None, acc=None):
    """構造キーの値に現れた cl_global_* のみを参照とみなす（散文中の言及は拾わない）。"""
    acc = set() if acc is None else acc
    if isinstance(node, dict):
        for k, v in node.items():
            structural_clause_refs(v, k, acc)
    elif isinstance(node, list):
        for v in node:
            structural_clause_refs(v, key, acc)
    elif isinstance(node, str) and key in REF_KEYS:
        acc.update(CLAUSE_RE.findall(node))
    return acc


def run(record_path, refs_dir):
    rec = load_json(record_path)
    results, notes = {}, []

    def check(label, ok, detail=""):
        results[label] = ("PASS" if ok else "FAIL", detail)

    def skip(label, reason):
        results[label] = ("SKIP", reason)

    units = rec.get("units", [])
    ids = [u.get("id") for u in units]
    spread_id = rec.get("spread_id", "")
    faces = set(spread_id.split("-"))

    gc_path = os.path.join(refs_dir, "global_clauses.json")
    ts_path = os.path.join(refs_dir, "typography_scale.json")

    registered, back_components = set(), []
    if os.path.exists(gc_path):
        gl = load_json(gc_path)
        registered = {c["id"] for c in gl.get("clauses", [])}
        for c in gl.get("clauses", []):
            for comp in c.get("components", []):
                back_components.append((c["id"], comp.get("spread"), comp.get("text_unit")))
            for rel in c.get("relations_in", []):
                frm = rel.get("from", "")
                if ":" in frm:
                    sp, tu = frm.split(":", 1)
                    back_components.append((c["id"], sp, tu))

    class_anchors, paratext_anchors, scale_ok = load_scale(ts_path)

    # 1-3 id
    dup = sorted({i for i in ids if ids.count(i) > 1})
    check(LABELS[0], not dup, str(dup))
    bad = [i for i in ids if not (isinstance(i, str) and ID_RE.match(i))]
    check(LABELS[1], not bad, str(bad))
    rh_all = rec.get("revision_history", [])
    bad = [(u.get("id"), why) for u in units
           for why in [face_chain_problem(u, rh_all)] if why]
    check(LABELS[2], not bad, str(bad))
    corrected = [u["id"] for u in units
                 if any(e.get("unit_id") == u.get("id") and e.get("field") == "face" for e in rh_all)]
    if corrected and not bad:
        notes.append("face 訂正の連鎖で説明された接頭辞の不一致: %d 件" % len(corrected))

    # 4-6 数量・面
    check(LABELS[3], rec.get("unit_count") == len(units),
          "%s vs %d" % (rec.get("unit_count"), len(units)))
    seqs = [u.get("seq") for u in units]
    dup = sorted({s for s in seqs if seqs.count(s) > 1})
    check(LABELS[4], not dup, str(dup))
    bad = sorted({u.get("face") for u in units} - faces)
    check(LABELS[5], not bad, str(bad))

    # 7-9 type_class（bool は int の派生型なので type() で厳格に除外）
    bad = [u["id"] for u in units
           if not (u.get("type_class") is None
                   or (type(u.get("type_class")) is int and u["type_class"] in (1, 2, 3, 4)))]
    check(LABELS[6], not bad, str(bad))

    nulls = [u for u in units if u.get("type_class") is None]
    if not nulls:
        skip(LABELS[7], "type_class=null のユニットが存在しない")
    elif not scale_ok:
        check(LABELS[7], False, "null ユニットがあるが typography_scale.json を参照できず照合不能")
    else:
        bad = [u["id"] for u in nulls if not u.get("note") or u["id"] not in paratext_anchors]
        check(LABELS[7], not bad, str(bad))

    if not scale_ok:
        skip(LABELS[8], "typography_scale.json が同梱されていないため錨照合を実施できない")
    else:
        overlap = [u for u in units if u["id"] in class_anchors]
        if not overlap:
            skip(LABELS[8], "本記録のユニットは typography_scale.json の錨に登録されていない")
        else:
            bad = [(u["id"], u.get("type_class"), class_anchors[u["id"]])
                   for u in overlap if u.get("type_class") != class_anchors[u["id"]]]
            check(LABELS[8], not bad, str(bad))
            notes.append("錨照合の対象: " + ", ".join(u["id"] for u in overlap))
        # 台帳側に登録されている錨のうち、本スプレッドを指しながら解決しないもの
        ghosts = [tu for tu in class_anchors
                  if tu.startswith(tuple("tu_%s_" % f for f in faces)) and tu not in ids]
        if ghosts:
            notes.append("typography_scale.json 側に本スプレッドを指す未解決の錨 ID: "
                         + ", ".join(sorted(ghosts)) + "（正本側ではなく錨表の未反映）")

    # 10-11 style
    bad = [u["id"] for u in units if u.get("style") not in STYLES]
    check(LABELS[9], not bad, str(bad))
    bad = [u["id"] for u in units if u.get("style") == "mixte" and not u.get("note")]
    check(LABELS[10], not bad, str(bad))

    # 12-13 訂正履歴
    rh = rec.get("revision_history", [])
    if not rh:
        skip(LABELS[11], "revision_history は空配列（訂正なし）")
    else:
        bad = [e for e in rh if not RH_KEYS.issubset(e.keys()) or e.get("field") not in ("text", "face")]
        check(LABELS[11], not bad, "%d 件中 %d 件が不適合" % (len(rh), len(bad)) if bad else "%d 件適合" % len(rh))
    dep = rec.get("deprecated_ids", [])
    if not dep:
        skip(LABELS[12], "deprecated_ids は空配列")
    else:
        bad = [e for e in dep if not DEP_KEYS.issubset(e.keys())]
        check(LABELS[12], not bad, "%d 件中 %d 件が不適合" % (len(dep), len(bad)) if bad else "%d 件適合" % len(dep))

    # 14-16 text
    bad = [u["id"] for u in units if "'" in str(u.get("text", ""))]
    check(LABELS[13], not bad, str(bad))
    bad = [u["id"] for u in units
           if unicodedata.normalize("NFC", str(u.get("text", ""))) != u.get("text")]
    check(LABELS[14], not bad, str(bad))
    bad = [u["id"] for u in units
           if not str(u.get("text", "")).strip() or u.get("text") != str(u.get("text", "")).strip()]
    check(LABELS[15], not bad, str(bad))

    # 17-18 台帳参照
    struct = sorted(structural_clause_refs(rec))
    if not struct:
        skip(LABELS[16], "構造キーによる cl_global_* 参照なし（level-0 は統語層を扱わない）")
    elif not registered:
        skip(LABELS[16], "構造参照 %d 件あるが global_clauses.json 未同梱" % len(struct))
    else:
        bad = [r for r in struct if r not in registered]
        check(LABELS[16], not bad, str(bad))

    if not os.path.exists(gc_path):
        skip(LABELS[17], "global_clauses.json 未同梱")
    else:
        bad = [(cid, tu) for cid, sp, tu in back_components
               if sp in faces | {spread_id} and tu not in ids]
        check(LABELS[17], not bad, str(bad))

    prose = sorted({m for s in walk_strings(rec) for m in CLAUSE_RE.findall(s)} - registered)
    if prose:
        notes.append("散文中で言及される未登録 clause: " + ", ".join(prose)
                     + "（構造参照ではないため合否に影響しない）")

    # 19 open_questions の二区分運用
    section = next((s for s in OQ_SECTIONS if rec.get(s)), None)
    if section is None:
        skip(LABELS[18], "open_questions / open_issues のいずれも空または不在")
    else:
        bad = [q.get("id") for q in rec[section]
               if q.get("status") not in ("open", "resolved", "closed")
               and q.get("category") != "pending_verbatim_collation"]
        unresolved = [q.get("id") for q in rec[section] if q.get("status") == "open"]
        detail = "節名 %s、%d 件" % (section, len(rec[section]))
        if unresolved:
            detail += "（未決 %s）" % ", ".join(unresolved)
        check(LABELS[18], not bad, str(bad) if bad else detail)
        if section != "open_questions":
            notes.append("本記録は open_questions ではなく %s を用いている（旧世代の節名）" % section)

    # 20 status
    check(LABELS[19], rec.get("status") in STATUS_VOCAB, repr(rec.get("status")))

    # 21 deprecated_ids の解決
    if not dep:
        skip(LABELS[20], "deprecated_ids は空配列")
    else:
        bad = deprecation_problems(dep, ids)
        check(LABELS[20], not bad, "; ".join(bad) if bad else "%d 件すべて解決" % len(dep))

    missing = [l for l in LABELS if l not in results]
    assert not missing, "未実行の検査があります: %s" % missing
    return rec, results, notes


def report(rec, results, notes, quiet=False):
    counts = {s: sum(1 for st, _ in results.values() if st == s) for s in ("PASS", "FAIL", "SKIP")}
    denom = counts["PASS"] + counts["FAIL"]
    head = "%s — units %s / status %s" % (rec.get("spread_id"), rec.get("unit_count"), rec.get("status"))
    print("=" * 78)
    print(head)
    print("=" * 78)
    if not quiet:
        width = max(len(l) for l in LABELS)
        for label in LABELS:
            state, detail = results[label]
            line = "[%s] %s" % (state, label.ljust(width))
            if detail and state != "PASS":
                line += "  — %s" % detail
            print(line)
        for n in notes:
            print("\n[INFO] %s" % n)
    tail = "（SKIP %d／合否母数から除外）" % counts["SKIP"] if counts["SKIP"] else ""
    print("\n%d/%d passed%s" % (counts["PASS"], denom, tail))
    return counts["FAIL"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", help="検査する正本レコード")
    ap.add_argument("--all", help="ディレクトリ内の *_level0.json をすべて検査")
    ap.add_argument("--refs", default=None,
                    help="global_clauses.json / typography_scale.json の所在（既定＝レコードと同じディレクトリ）")
    ap.add_argument("--labels", action="store_true", help="LABELS を正典順に出力して終了")
    ap.add_argument("--quiet", action="store_true", help="集計のみ出力")
    args = ap.parse_args()

    if args.labels:
        print("\n".join(LABELS))
        return 0

    if args.all:
        paths = sorted(glob.glob(os.path.join(args.all, "*_level0.json")),
                       key=lambda p: int(re.search(r"f(\d+)", os.path.basename(p)).group(1)))
    elif args.record:
        paths = [args.record]
    else:
        ap.error("--record か --all のいずれかが必要です")

    fails = 0
    for p in paths:
        refs = args.refs or os.path.dirname(os.path.abspath(p))
        rec, results, notes = run(p, refs)
        fails += report(rec, results, notes, quiet=args.quiet)
    if len(paths) > 1:
        print("\n" + "=" * 78)
        print("%d 本を検査、FAIL のあるレコード %d 本" % (len(paths), fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
