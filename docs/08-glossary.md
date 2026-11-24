# 08 · Glossary

Terms are given in English with the Japanese working term where one is in use. Where a term's application is still being unified across the corpus, this is stated rather than smoothed over.

| Term | 日本語 | Definition |
|---|---|---|
| **face** | 面 | A physical page‑face, `f1`–`f23`. Every text unit belongs to exactly one face. A misrecorded face is corrected in place through `revision_history`; the identifier keeps the face at issue. |
| **spread** | 見開き | A pair of facing faces, and the unit of one level‑0 record file. |
| **text unit** | テクスト単位 | The addressable atom, `tu_<face>_<slug>`. Extent decided by physical layout, not by sense. |
| **level‑0** | level‑0 / 観察層 | The observation record. The minimum depth at which citability is guaranteed. |
| **layer** | 層 | An interpretive artefact attached to level‑0 by identifier, separately authored and versioned. |
| **type_class** | 級 | Integer 1–4 for the four measured type sizes (14 / 5 / 4 / 3 mm). `null` for paratext outside the census. |
| **census** | 級台帳 | The approved inventory of type sizes with measured anchors. Outranks per‑image estimation. |
| **anchor** | 錨 | A specific ruler‑measured occurrence registered as evidence for a size class. Drawn from the poem body only. |
| **paratext sizes** | パラテクスト寸法 | Clause holding measured paratext elements that match a class but are not promoted to anchors. |
| **style** | 書体 | `romain` / `italique` / `mixte`. `mixte` requires a note; typeface alone never splits a unit. |
| **seq** | 通し番号 | Provisional linearisation in steps of 10. Iteration convenience; **not part of the canonical address**. |
| **status** | 記録状態 | `draft_awaiting_collation` (default) / `awaiting_collation` / `awaiting_verbatim_collation` / `collated_with_original`. Independent of `record_depth`. |
| **record_depth** | 記録深度 | The depth at which a record is written; presently `level-0` throughout. |
| **deprecated_ids** | 廃止 ID | Required top‑level array retiring an identifier via `superseded_by` (a list of successors when a unit is split). Used for changes of extent, not for face corrections. Empty array when unused. |
| **revision_history** | 改訂履歴 | Post‑canonicalisation corrections: `date`, `unit_id`, `field`, `before`, `after`, `evidence`, `by`. |
| **open question** | 未決事項 | A published unresolved matter. `status: open` = design judgement pending; `category: pending_verbatim_collation` = to be settled by checking the copy. |
| **global clause** | 全体節 | A syntactic clause spanning multiple spreads, registered in `data/global/`. Level‑0 records may be referenced by one; they do not assert one. |
| **sigla** | シグラ | Interpreter code on a layer claim. C = Cohn, D = Davies, M = Marchal, K = Kristeva, G = Favre/Garnier, N = Nagakura. |
| **witness** | 参照証人 | An edition consulted for comparison but never used as base text. |
| **gutter‑crossing line** | 中溝跨ぎ行 | A printed line whose fragments lie on both faces of a spread. Since level‑0 2.0.0 it is always recorded as one unit per face. See the note below on the term. |
| **SKIP** | SKIP | Validator outcome for a check with no applicable target, or whose optional dependency file is absent. Excluded from the pass/fail denominator. |

## Note on "gutter‑crossing line" (中溝跨ぎ行)

**Unit extent no longer depends on this term.** Since level‑0 2.0.0, every physical line that crosses the gutter is recorded as one unit per face. This holds whether the two faces are one sheet (f12–f13, the centre of the gathering) or two (f16–f17), and it matches the separated pairs of f8–f9 and f6–f7. Each fragment's `note` names its counterpart. Whether the spread is a single sheet is recorded once, in `physical_observations`. Joining the fragments is a syntax‑layer act. See [`migrations/2.0.md`](migrations/2.0.md).

What remains open is the term itself, as used in prose. In v1.1 the term was applied on two criteria:

- **Continuous setting criterion** — the fragments form one continuously set line that happens to cross the gutter (used at f14–f15 and f6–f7, where a shared baseline without continuous setting was held *not* to be a gutter‑crossing line);
- **Shared baseline criterion** — the fragments share a baseline across the two faces, whether or not the setting is continuous (used at f16–f17).

Settling this requires a decision about whether the term names a physical fact about setting or a physical fact about position, and that decision belongs with the layout layer. Until then, records state the observed situation explicitly (shared baseline; distance between fragments; whether the setting is continuous) rather than relying on the term.
