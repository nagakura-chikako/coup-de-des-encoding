# provenance/

*Integration proposals, frozen at the moment they were proposed.*

## What this directory is

The files here are **integration proposals** — drafts that proposed a change to a
canonical file. Every one of them has since been integrated. They are kept because
the canonical records cite them **by filename**, and a citation that resolves to
nothing is a broken record.

They are **not** part of the citable dataset. Nothing in this directory should be
read as a current statement about the encoding. For the current state, read the
canonical files in `data/`.

## Why these files must be published

Four of the twelve level-0 records, both registries, and the schema name these
files in their own text:

| File | Cited by |
|---|---|
| `typography_scale_update_2026-07-16.json` | `typography_scale.json` |
| `typography_scale_update_2026-07-20.json` | **f16-f17**, `typography_scale.json` |
| `typography_scale_update_2026-07-22.json` | **f18-f19**, `global_clauses.json`, `typography_scale.json` |
| `typography_scale_update_2026-07-22b.json` | **f20-f21**, **f22-f23**, `typography_scale.json` |
| `typography_scale_update_2026-07-25.json` | **f1**, `level0_schema.json`, `typography_scale.json` |
| `level0_schema_update_2026-08-24.json` | `level0_schema.json` |

A record that says "see the update of 2026-07-22 for the integration" is making a
verifiable claim. Publishing the dataset without these files would leave that claim
unverifiable.

## The preservation rule

**These files are frozen. Nothing in them is updated to the present tense.**

Two consequences are worth stating plainly, because both look like errors and
neither is one:

**1. `integration_status` may say the work is not yet done.**
`typography_scale_update_2026-07-25.json` contains
`"state": "proposal_not_yet_integrated"` and lists remaining work on
`typography_scale.json` and `level0_schema.json`. That was accurate on 2026-07-25.
Both integrations were completed on 2026-07-26 and 2026-07-27. The sentence is not
corrected, because the file records what was true when the proposal was made.

**For the current integration status, the canonical files are authoritative** —
`typography_scale.json` (`integration_status`) and `level0_schema.json`
(`revisions`), not the statements inside any file in this directory.

**2. Apostrophes are not normalised here.**
The project normalises apostrophes to U+2019 across the dataset, and
`global_clauses.json` treats U+0027 as a validation error. That rule governs the
canonical records and registries. Three files here
(`...07-16`, `...07-22`, `...07-25`) still contain U+0027 in prose and in some
`anchor_word` values; the values were normalised when they were integrated, so the
canonical anchors carry U+2019. The proposals are left as they were written.

Applying either correction retroactively would make these files agree with the
present at the cost of no longer recording the past. That trade is not worth making
for documents whose only job is to record the past.

## Contents

**`typography_scale_update_2026-07-16.json`** — Completes size class 1: anchors
UN COUP DE DÉS (f3) and JAMAIS (f5) at 14 mm, making all four components of the
capital sentence fully measured. Also records the relation to the authorial layer
(the maquette's marginal figures 36 / 36-over-28 / 28 split within a sentence that
Ronat realises as a single tier).

**`typography_scale_update_2026-07-20.json`** — Adds the class 2 anchor SI (f17,
5 mm), and measures the double protrusion of the italic lowercase *f*: nominally
4 mm, it spans 5 mm — the cap height of SI itself.

**`typography_scale_update_2026-07-22.json`** — Six anchors from f18-f19, the only
spread where all four census tiers occur together. Establishes that size, face, and
capitalisation are three independent axes.

**`typography_scale_update_2026-07-22b.json`** — Adds the class 3 anchor
N'AURA EU LIEU (f21). The second capital sentence sits, capitals and all, at 4 mm:
the two central sentences are distinguished within the typography-scale model by
size alone.

**`typography_scale_update_2026-07-25.json`** — Implements the ruling on
`oq_l0_f1_poeme_8mm`: a `paratext_sizes` annex holding POÈME (f1, 8 mm) outside the
four body tiers, and the schema rule permitting `type_class: null` for measured
paratext sizes outside the census.

**`level0_schema_update_2026-08-24.json`** — Adds `record_generations` and
`optional_fields` to the schema, giving it the vocabulary to describe twenty
previously undefined keys across the twelve records. Unlike the files above, this
one carries `integration_status: integrated_into_level0_schema_2026-08-24`, because
it was written after the convention of recording integration was established.

## Two files that were replaced rather than integrated

`typography_scale_update_2026-07-12c.json` and `..._2026-07-12d.json` sit apart from
the rest. The others are proposals that were integrated: what they proposed is in the
canonical file, and `typography_scale.json` lists them under `integrated_updates`.
These two are not listed there, and they should not be.

They belong to a moment when the numbering of the size classes was itself in motion.
`-12c` abolished the provisional class 3 and folded it into class 4, and created a
tier identified as `5mm_si`; `-12d` renamed that tier and added a `3mm` class. Neither
identifier exists today: the current census is `size_class` 1 to 4. What replaced
these proposals was not an integration but a change of the system they were written
in, and `typography_scale.json` records that separately, under `superseded`.

They are kept because the census summary in `-12d` — four tiers only, all four present
together on f18-f19 and nowhere else, the coda returning to the 4 mm plain — is the
direct ancestor of the description in the canonical file. Reading them shows what the
model looked like one revision before it settled.

## A note on duplicates

Two byte-identical copies (`...22b-2.json`, `...25-2.json`) arose during file
transfer and are not included. They were verified identical to the published files
at the byte level; no information is lost by their absence.

---

# provenance/（日本語）

*統合前の提案を、提案された時点のまま凍結して保存する。*

## このディレクトリについて

ここにあるのは、正典ファイルへの変更を提案した**統合案**です。いずれもすでに統合
済みです。これらを保存しているのは、正典レコードがこれらを**ファイル名で名指しして
いる**ためで、解決しない参照を抱えたレコードは、それ自体が壊れた記録になります。

これらは**引用対象のデータセットではありません**。エンコーディングの現在の状態を
述べたものとして読まないでください。現在の状態は `data/` の正典ファイルにあります。

## 公開が必要な理由

level-0 正本12本のうち4本、台帳2点、schema が、これらのファイルを本文中で名指しして
います（上表参照）。「2026-07-22 の update を参照」と書かれた記録は、検証可能な主張を
しています。これらを同梱せずに公開すれば、その主張は検証不能になります。

## 保存の原則

**これらのファイルは凍結されています。現在形への書き換えは行いません。**

誤りに見えるが誤りではないものが2つあるので、明記します。

**1. `integration_status` が「未統合」と述べている場合がある。**
`typography_scale_update_2026-07-25.json` は `"state": "proposal_not_yet_integrated"`
を持ち、`typography_scale.json` と `level0_schema.json` への残作業を挙げています。
これは 2026-07-25 時点では正確でした。両方の統合は 2026-07-26 と 2026-07-27 に完了して
います。この記述を訂正しないのは、このファイルが提案時点の事実を記録するものだから
です。

**現在の統合状況は正典ファイルを正とします**——`typography_scale.json` の
`integration_status`、および `level0_schema.json` の `revisions`。本ディレクトリの
ファイル内の記述ではありません。

**2. アポストロフはここでは正規化されていない。**
本プロジェクトはアポストロフを U+2019 に統一し、`global_clauses.json` は U+0027 の混入
を検証エラーとします。この規則が及ぶのは正典レコードと台帳です。ここにある3点
（`...07-16`／`...07-22`／`...07-25`）は散文と一部の `anchor_word` に U+0027 を含んだ
ままですが、統合の際に値は正規化されており、**正典側の錨は U+2019 です**。提案文書は
書かれたときのまま残します。

どちらの訂正も、ファイルを現在と一致させる代わりに、過去を記録しなくさせます。過去を
記録することだけが仕事の文書について、その取引は割に合いません。

## 収録ファイル

**`typography_scale_update_2026-07-16.json`** — class 1 の完結。UN COUP DE DÉS（f3）
と JAMAIS（f5）を 14mm で錨として追加し、表題文4成分の全点実測が完了。著者指示層との
関係（マケット欄外数字 36／36 en surcharge 28／28 の文内分割を、Ronat は単一層として
実現している）も記録。

**`typography_scale_update_2026-07-20.json`** — class 2 の錨 SI（f17、5mm）を追加。
あわせてイタリック小文字 *f* の上下突き抜けを実測——公称 4mm に対し実質全高 5mm で、
SI のキャップ高に達する。

**`typography_scale_update_2026-07-22.json`** — f18-f19 からの錨6点。census 全4層が
共存する詩中唯一の見開きであり、サイズ・書体・大文字性が三つの独立した軸であることを
確定させた。

**`typography_scale_update_2026-07-22b.json`** — class 3 の錨 N'AURA EU LIEU（f21）を
追加。第2の中心文は大文字のまま 4mm に置かれ、typography-scale モデルの内部で2つの
中心文を区別する軸はサイズのみとなる。

**`typography_scale_update_2026-07-25.json`** — `oq_l0_f1_poeme_8mm` の裁定の実装。
本文 census 4層の外側に `paratext_sizes` 附属節を設けて POÈME（f1、8mm）を記録し、
census 外のパラテクスト実測サイズに `type_class: null` を許容する schema 規則を提案。

**`level0_schema_update_2026-08-24.json`** — schema に `record_generations` と
`optional_fields` を新設し、12本のレコードに現れる未定義キー20件を記述できるようにした
もの。上記5点と異なり `integration_status: integrated_into_level0_schema_2026-08-24` を
持つ——統合状況を記録する慣行が確立した後に書かれたため。

## 重複について

バイト単位で同一の複製2点（`...22b-2.json`／`...25-2.json`）はファイル転送の過程で
生じたもので、公開セットには含めません。公開版とバイト単位の同一性を確認済みであり、
不在によって失われる情報はありません。
