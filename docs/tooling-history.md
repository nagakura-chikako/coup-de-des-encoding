# Tooling history

*How the validation tools came to be, and why the earlier ones are not shipped.*

## Current tools

Everything you need to validate this dataset is in `tools/`, and consists of three
files:

| File | What it does |
|---|---|
| `check_level0.py` | Checks one record — or all twelve — against the twenty‑one `machine_checks` declared in `level0_schema.json` (twenty until 2.0.0). `--record`, `--all`, `--refs`, `--labels`, `--quiet` |
| `verify_sync.py` | Checks the *relationship* between schema, records, and checker: label synchronisation, template coverage, and the fingerprint of the immutable unit fields |
| `units_manifest.json` | The fingerprint ledger — 12 records, 224 units. `verify_sync.py` compares against it |

**Nothing else should be run against this dataset.** This document exists because
those three files had predecessors, and the predecessors are worth describing even
though they are not published.

## Why the earlier checkers are not in this repository

Between 2026-07-24 and 2026-07-28, each spread was validated by its own checker:
`check_f1`, `check_f2f3`, `check_f4f5`, `check_f6f7`, `check_f8f9`, alongside an
early `verify_sync`. They were consolidated into `check_level0.py` on 2026-08-24.

They are not shipped for one reason: **they are executable, and none of them is
usable now.** A stale prose document invites reading; a stale script invites
running. Two of them would fail loudly, which is harmless. One of them fails
*quietly* — and that is the case that matters (see "The `size_class` bug" below).

Their absence does not erase them. The history of the records themselves is carried
inside the published data: `provenance_note`, `revision_history`, `deprecated_ids`,
`open_questions`, and the schema's `record_generations`. What the earlier checkers
carry is a different history — the history of the *tooling* — and it is described
here rather than shipped as runnable code.

## The five spread checkers

| Checker | Written | Target | What it contributed | State now |
|---|---|---|---|---|
| `check_f1` | 2026-07-24/25 | f1 | First implementation of the paratext rule permitting `type_class: null` | **Superseded.** Reads anchors from `typography_scale_update_2026-07-25.json`, integrated into the main file on 2026-07-27. 10 checks only |
| `check_f2f3` | 2026-07-25 | f2-f3 | First to make "is the registry file present?" a check in its own right — the germ of the later three-valued verdict | **Superseded.** 12 checks. Applies the U+0027 rule to the whole file rather than to `text` |
| `check_f4f5` | 2026-07-26 | f4-f5 | Cross-record ID uniqueness, checked against another record and the registry | **Not runnable.** Absolute paths hard-coded to one session's working directory. Its text pattern accepts capitals only |
| `check_f6f7` | 2026-07-27 | f6-f7 | **The reference implementation.** Three-valued PASS/FAIL/SKIP, `--labels` synchronised with the schema, `__file__`-relative paths, structural-key scanning for clause references | **Superseded, and carries a silent bug** (below) |
| `check_f8f9` | 2026-07-28 | f8-f9 | `--record` / `--refs` arguments — the first move toward a general checker — and the correct anchor key name | **Superseded.** Its labels are twenty-one English strings, not synchronised with the schema's twenty; its required-key list assumes the generation-C record shape and cannot be applied to earlier records |

Two design decisions from this period survive unchanged in `check_level0.py`:

**The three-valued verdict.** A check with nothing to check, or one whose optional
dependency is not present, returns SKIP and is excluded from the denominator. The
alternative — counting it as a failure — makes the absence of an optional file look
like a defect in the data. This came from `check_f6f7`.

**Label synchronisation.** The checker's labels are a canonical-order constant,
printable with `--labels`, and `verify_sync.py` compares them against the schema
string by string. A check that exists in the schema but not in the code, or the
reverse, is itself a finding. This also came from `check_f6f7`.

`check_f8f9` contributed the argument interface and, as it happens, the one line
that the reference implementation had wrong.

## The `size_class` bug

`check_f6f7` looked up the size class of a typographic anchor by trying the keys
`class`, `class_id`, `type_class`, and `id`. The key in `typography_scale.json` is
`size_class`. It was not among the candidates.

The consequence was not an error. The lookup found no anchors, concluded that this
spread had none registered, and reported:

```
[SKIP] typography_scale.json の錨と type_class が一致
       — 本記録のユニットは typography_scale.json の錨に登録されていない
```

This is false. f6-f7 has two registered anchors. The check had not been performed,
and said so in words that meant something else. It went unnoticed for roughly a
month — the SKIP looked like the familiar, legitimate "dependency not bundled" case,
and the summary line showed no failure.

It surfaced on 2026-08-24, while the generation checkers were being read side by
side to write `check_level0.py`. `check_f8f9`, written a day after `check_f6f7`,
used `size_class` correctly. The two implementations disagreed, and the
disagreement was the signal. No single implementation could have revealed it.

Three things follow, and all three are in the current tools:

1. `check_level0.py` tries `size_class` first, keeping the other names only as
   fallbacks.
2. A SKIP is not evidence that a check passed. It is evidence that a check did not
   run. Its stated reason is a claim like any other, and can be wrong.
3. When an anchor names a unit belonging to the spread under test but does not
   resolve, `check_level0.py` now emits an INFO line saying so explicitly, and
   attributes the gap to the anchor table rather than to the record. Silence was
   the failure mode; naming the discrepancy is the fix.

## Generations

The records themselves fall into three generations of format (see
`record_generations` in `level0_schema.json`). The checkers ran a generation behind:
they were written for generation C, which is why `check_f8f9`'s required-key list
cannot be applied to the seven earlier records. Consolidating into one checker meant
teaching it to read all three — hence its acceptance of both `open_questions` and
`open_issues`, and of both shapes of `physical_observations`.

That is the general shape of what happened here. The encoding format changed twice
while the corpus was being recorded, and the validation tooling had to learn to
describe what existed rather than to enforce what came last.

## Where the code is

Not in this repository. A companion repository on the making of this dataset — the
division of labour between human judgement and machine proposal — is planned, and
the checkers belong there, with the sessions that produced them. Until then this
document is the record of their existence.

---

# 検査ツールの成立史（日本語）

*検査ツールがどう成立したか、そして旧世代のツールをなぜ同梱しないか。*

## 現行ツール

本データセットの検証に必要なものは `tools/` の3ファイルに集約されています。

| ファイル | 役割 |
|---|---|
| `check_level0.py` | 1本のレコード、または12本すべてを、`level0_schema.json` の `machine_checks` 21項目（2.0.0 までは20項目）に照らして検査する。`--record`／`--all`／`--refs`／`--labels`／`--quiet` |
| `verify_sync.py` | schema・レコード・checker の**三者の関係**を検査する。ラベルの同期、テンプレートの充足、`units` 不変項目の指紋照合 |
| `units_manifest.json` | 指紋台帳（12レコード・224ユニット）。`verify_sync.py` が照合する |

**これ以外を本データセットに対して実行しないでください。**本文書があるのは、この3点に
前身があり、同梱しないとしても記述する価値があるからです。

## 旧 checker を同梱しない理由

2026-07-24 から 07-28 にかけて、各見開きはそれぞれ専用の checker で検査されていました
（`check_f1`／`check_f2f3`／`check_f4f5`／`check_f6f7`／`check_f8f9`、および初期の
`verify_sync`）。2026-08-24 に `check_level0.py` へ統合されています。

同梱しない理由は一つです。**それらは実行可能であり、かつ現在はどれも使えない**から
です。古い散文は読まれるだけですが、古いスクリプトは実行されます。うち2点は派手に
落ちるので無害です。1点は**静かに誤ります**——問題はそこにあります（後述）。

同梱しないことは、それらを消すことではありません。レコード自身の成立史は公開データの
内部に実装されています——`provenance_note`、`revision_history`、`deprecated_ids`、
`open_questions`、そして schema の `record_generations`。旧 checker が担うのはそれとは
別の、**ツールの成立史**であり、実行可能なコードとしてではなく、ここに記述として残し
ます。

## 5本のスプレッド専用 checker

| checker | 作成 | 対象 | 何を寄与したか | 現在の状態 |
|---|---|---|---|---|
| `check_f1` | 2026-07-24/25 | f1 | `type_class: null` を許容する paratext 規則の初実装 | **旧仕様。** 錨を `typography_scale_update_2026-07-25.json` から読むが、同ファイルは 2026-07-27 に本体へ統合済み。検査は10項目のみ |
| `check_f2f3` | 2026-07-25 | f2-f3 | 「台帳ファイルが存在するか」を独立した検査にした最初の例——後の三値判定の萌芽 | **旧仕様。** 12項目。U+0027 の規則を `text` ではなくファイル全域に適用している |
| `check_f4f5` | 2026-07-26 | f4-f5 | 他レコードおよび台帳と突き合わせた ID 全域一意性の検査 | **実行不能。** 特定セッションの作業ディレクトリへの絶対パス直書き。`text` の正規表現が大文字のみを許す |
| `check_f6f7` | 2026-07-27 | f6-f7 | **参照実装。**三値判定 PASS／FAIL／SKIP、schema と同期した `--labels`、`__file__` 基準のパス、節参照の構造キー走査 | **旧仕様。かつ静かに誤るバグを持つ**（後述） |
| `check_f8f9` | 2026-07-28 | f8-f9 | `--record`／`--refs` 引数——汎用化への最初の一歩——と、正しい錨キー名 | **旧仕様。** ラベルが英語21項目で schema の20項目と非同期。必須キー一覧が世代C のレコード形式を前提としており、それ以前の世代には適用できない |

この時期の設計判断のうち2つは、`check_level0.py` にそのまま生きています。

**三値判定。**適用対象のない検査、および任意の依存ファイルが不在の検査は SKIP とし、
合否の母数から除外する。これを失敗として数えると、任意ファイルの不在がデータの欠陥の
ように見えてしまう。`check_f6f7` 由来です。

**ラベルの同期。**checker のラベルは正典順の定数であり、`--labels` で出力でき、
`verify_sync.py` が schema と一字一句照合する。schema にあってコードにない検査、あるいは
その逆は、それ自体が発見となる。これも `check_f6f7` 由来です。

`check_f8f9` は引数インターフェースを寄与し、そしてたまたま、参照実装が誤っていた1行を
正しく書いていました。

## `size_class` のバグ

`check_f6f7` は活字錨のサイズクラスを、`class`／`class_id`／`type_class`／`id` の順に
キーを試して取得していました。`typography_scale.json` の実際のキーは `size_class` で、
候補に入っていませんでした。

結果はエラーではありませんでした。錨が1件も見つからず、この見開きには錨が登録されて
いないと判断し、こう報告しました。

```
[SKIP] typography_scale.json の錨と type_class が一致
       — 本記録のユニットは typography_scale.json の錨に登録されていない
```

これは誤りです。f6-f7 には錨が2点登録されています。検査は実行されておらず、しかもそれを
別の意味に読める言葉で報告していました。約1か月のあいだ気づかれませんでした——SKIP は
「依存ファイル未同梱」という馴染みのある正当なケースに見え、集計行にも失敗は現れなかった
からです。

発覚したのは 2026-08-24、`check_level0.py` を書くために各世代の実装を並べて読んでいた
ときでした。`check_f6f7` の翌日に書かれた `check_f8f9` は `size_class` を正しく使って
いました。二つの実装が食い違い、その食い違いが信号になった。**単一の実装だけでは
発見できませんでした。**

ここから3つのことが導かれ、いずれも現行ツールに反映されています。

1. `check_level0.py` は `size_class` を第一候補とし、他の名前はフォールバックとしてのみ
   残す。
2. SKIP は検査が通った証拠ではない。検査が**実行されなかった**証拠である。そこに書かれた
   理由は他の主張と同じく一つの主張であり、誤りうる。
3. 検査対象のスプレッドに属するユニットを名指しながら解決しない錨があるとき、
   `check_level0.py` は INFO 行でそれを明示し、齟齬の所在を正本側ではなく錨表側に帰属
   させる。沈黙が失敗の様態だったので、齟齬に名前を与えることが修正になる。

## 世代について

レコード自身は3つの記録形式の世代に分かれます（`level0_schema.json` の
`record_generations` 参照）。checker は一世代遅れて走っていました——いずれも世代C を
前提に書かれており、`check_f8f9` の必須キー一覧がそれ以前の7本に適用できないのはその
ためです。一本の checker へ統合するとは、三世代すべてを読めるように教えることでした
——`open_questions` と `open_issues` の双方を、`physical_observations` の二つの型を、
ともに受け入れるのはそのためです。

ここで起きたことの形は、そういうものです。コーパスを記録している途中で記録形式が二度
変化し、検査ツールは、最後に来たものを強制するのではなく、現に存在するものを記述する
ことを学ばなければならなかった。

## コード本体の所在

本リポジトリにはありません。本データセットの制作について——人間の判断と機械の提案の
切り分けについて——扱う姉妹リポジトリを予定しており、旧 checker はそれを生んだセッション
とともに、そちらに収録されます。それまでは、本文書がその存在の記録です。
