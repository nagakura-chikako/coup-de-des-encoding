#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_sync.py — schema・record・checker の相互整合を検証する（全スプレッド共通）。

check_level0.py が「1本のレコードが schema の machine_checks を満たすか」を見るのに対し、
本スクリプトは三者の関係そのものを見る：

  schema 層（1回だけ実行）
    A. schema.validation.machine_checks ⇔ checker の LABELS が一字一句同期
    B. schema が参照する内部名（doctrine.upgrade_path 等）の実在
    C. 改訂済みキー（dependency_pending）が構造上に残存しない
    D. schema_version の据え置き

  レコード層（各正本について実行）
    E. record が record_template の全キーを備える
    F. 全 unit のフィールド集合が template と一致
    G. field_definitions 未定義のトップレベルキー（情報提示・合否に影響しない）
    H. unit 不変項目（id/face/seq/text/type_class/style）の指紋が manifest と一致

H の manifest は、level-0 の正本が「引用可能性を保証する層」である以上、
units が意図せず変化していないことを後から機械的に示すためのもの。
初回は --update-manifest で生成し、以後は照合に用いる。

usage:
    python3 verify_sync.py --all DIR --schema PATH --checker PATH
    python3 verify_sync.py --record f14-f15_level0.json --schema ... --checker ...
    python3 verify_sync.py --all DIR --schema ... --checker ... --update-manifest
"""

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT_INVARIANTS = ["id", "face", "seq", "text", "type_class", "style"]

ok = True
def line(tag, msg):
    """tag ∈ {OK, NG, --}。'--' は情報提示で合否に影響しない。"""
    global ok
    if tag == "NG":
        ok = False
    print("[%s] %s" % (tag, msg))


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def fingerprint(units):
    payload = [[u.get(k) for k in UNIT_INVARIANTS] for u in units]
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()[:16]


def keys_anywhere(node, acc=None):
    acc = set() if acc is None else acc
    if isinstance(node, dict):
        acc.update(node.keys())
        for v in node.values():
            keys_anywhere(v, acc)
    elif isinstance(node, list):
        for v in node:
            keys_anywhere(v, acc)
    return acc


def verify_schema(sch, checker_path):
    print("── schema 層 " + "─" * 62)

    # A. machine_checks ⇔ checker LABELS
    try:
        labels = subprocess.run([sys.executable, checker_path, "--labels"],
                                capture_output=True, text=True, check=True).stdout.splitlines()
    except (subprocess.CalledProcessError, OSError) as exc:
        line("NG", "checker から LABELS を取得できない（%s）: %s" % (checker_path, exc))
        labels = None

    mc = sch["validation"]["machine_checks"]
    if labels is not None:
        same = mc == labels
        line("OK" if same else "NG",
             "machine_checks ⇔ checker LABELS 同期（%d 項目、順序含め一致: %s）" % (len(mc), same))
        if not same:
            for i, (a, b) in enumerate(zip(mc, labels), 1):
                if a != b:
                    print("      %2d. schema : %s" % (i, a))
                    print("          checker: %s" % b)
            if len(mc) != len(labels):
                print("      項目数が異なる: schema %d / checker %d" % (len(mc), len(labels)))

    # B. schema が参照する内部名の実在
    up = "upgrade_path" in sch.get("doctrine", {})
    imm = any(i.get("id") == "oq_l0_id_immutability_rules_reference"
              for i in sch.get("resolutions", {}).get("items", []))
    line("OK" if up and imm else "NG",
         "id_immutability_rules の参照先 doctrine.upgrade_path が実在（%s）／明文化済み（%s）" % (up, imm))

    # C. 改訂済みキーの残存（散文中の言及は改訂の記録そのものなので構造走査で判定）
    ks = keys_anywhere(sch)
    line("OK" if "dependency_pending" not in ks else "NG",
         "dependency_pending がキーとして残存しない（dependency_resolution 有: %s）"
         % ("dependency_resolution" in ks))

    # D. schema_version
    line("OK" if sch.get("schema_version") == "0.3" else "NG",
         "schema_version = %s（据え置き）" % sch.get("schema_version"))


def verify_record(rec, sch, manifest, update):
    sid = rec.get("spread_id", "?")
    units = rec.get("units", [])
    print("\n── %s " % sid + "─" * max(4, 70 - len(sid)))

    # E. record_template のキー充足
    tmpl = set(sch["record_template"].keys()) - {"units"}
    missing = sorted(tmpl - set(rec.keys()))
    line("OK" if not missing else "NG",
         "record が record_template の全キーを備える（欠落: %s）" % (missing or "なし"))

    # F. unit のフィールド集合
    tf = set(sch["record_template"]["units"][0].keys())
    bad = [u.get("id") for u in units if set(u.keys()) != tf]
    line("OK" if not bad else "NG",
         "全 unit のフィールド集合が template と一致（不一致: %s）" % (bad or "なし"))
    if bad:
        for u in units:
            if set(u.keys()) != tf:
                print("      %s: 余分 %s / 欠落 %s"
                      % (u.get("id"), sorted(set(u.keys()) - tf) or "なし",
                         sorted(tf - set(u.keys())) or "なし"))

    # G. field_definitions 未定義キー（情報提示）
    described = {k.split(".")[0] for k in sch.get("field_definitions", {})}
    undocumented = sorted(set(rec.keys()) - described - {"file", "schema_version", "schema_ref"})
    line("--", "field_definitions 未定義のレコード固有キー: %s" % (undocumented or "なし"))

    # H. unit 不変項目の指紋
    fp = fingerprint(units)
    n = len(units)
    line("OK" if rec.get("unit_count") == n else "NG",
         "unit_count = %s / units = %d" % (rec.get("unit_count"), n))

    entry = manifest.get("records", {}).get(sid)
    if update or entry is None:
        manifest.setdefault("records", {})[sid] = {"unit_count": n, "fingerprint": fp}
        line("--", "unit 不変項目の指紋: %s（manifest に%s）"
             % (fp, "更新" if entry else "新規登録"))
    else:
        same = entry.get("fingerprint") == fp and entry.get("unit_count") == n
        line("OK" if same else "NG",
             "unit 不変項目の指紋が manifest と一致（%s）" % fp)
        if not same:
            print("      manifest: units %s / %s" % (entry.get("unit_count"), entry.get("fingerprint")))
            print("      現在    : units %d / %s" % (n, fp))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", help="検証する正本レコード")
    ap.add_argument("--all", help="ディレクトリ内の *_level0.json をすべて検証")
    ap.add_argument("--schema", default=os.path.join(HERE, "level0_schema.json"))
    ap.add_argument("--checker", default=os.path.join(HERE, "check_level0.py"))
    ap.add_argument("--manifest", default=os.path.join(HERE, "units_manifest.json"),
                    help="unit 不変項目の指紋台帳")
    ap.add_argument("--update-manifest", action="store_true",
                    help="指紋を照合せず manifest を現状で書き換える（初回生成・意図した改訂の後）")
    args = ap.parse_args()

    if args.all:
        paths = sorted(glob.glob(os.path.join(args.all, "*_level0.json")),
                       key=lambda p: int(re.search(r"f(\d+)", os.path.basename(p)).group(1)))
    elif args.record:
        paths = [args.record]
    else:
        ap.error("--record か --all のいずれかが必要です")

    sch = load_json(args.schema)
    manifest = load_json(args.manifest) if os.path.exists(args.manifest) else {}
    before = json.dumps(manifest, ensure_ascii=False, sort_keys=True)

    verify_schema(sch, args.checker)
    for p in paths:
        verify_record(load_json(p), sch, manifest, args.update_manifest)

    after = json.dumps(manifest, ensure_ascii=False, sort_keys=True)
    if after != before:
        manifest["generated"] = datetime.date.today().isoformat()
        manifest["schema_version"] = sch.get("schema_version")
        manifest["unit_invariants"] = UNIT_INVARIANTS
        with open(args.manifest, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)
            fh.write("\n")
        print("\n[--] manifest を書き出しました: %s" % args.manifest)

    print("\n" + ("相互整合 OK" if ok else "相互整合に問題あり"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
