# 10 · Open questions

There is no single ledger file. Each open question is carried inside the canonical file it arose in, in a machine-readable field: `open_items` in `data/global/typography_scale.json`, `open_questions` in the spread records, `status_note.grounds` in `data/global/proof_states.json`. This page explains how to read them, and why they are not collected into one place.

The reason is the one that governs the rest of the project: the file in which a question arose is the file that answers it. A separate ledger would be a second copy of a status whose authority lies elsewhere, and a second copy drifts. Reading a canonical file therefore always shows what is unresolved *about that file*, without a lookup.

## Why they are published

Because a reader needs to distinguish three states that look identical in a finished‑looking edition:

- decided, with reasons;
- undecided, and known to be undecided;
- never noticed.

Only the third is a defect. Publishing the second is what makes the claim about the first credible.

## Two categories

| Field | Meaning | Resolution requires |
|---|---|---|
| `status: open` | A design judgement is pending. | A decision, recorded with its reasoning. |
| `category: pending_verbatim_collation` | The answer exists on the page; nobody has checked it yet. | Access to the copy. No judgement. |

Keeping these apart matters: the first is an invitation to argue, the second is an invitation to look.

## Resolution

An open question is resolved by adding a resolution entry — decision, date, evidence, decider — and setting `status: resolved`. **The question is not deleted.** The record of a question that turned out to be a pseudo‑problem is worth as much as the record of a real one; one of this project's early questions dissolved when the photograph showed the disputed feature did not exist, and preserving that is more useful than tidying it away.

## Standing questions at v2.0

Illustrative rather than exhaustive; the canonical files are authoritative.

- **Corpus‑wide terminology: "gutter‑crossing line".** Two criteria in circulation (continuous setting vs shared baseline). Since 2.0.0 unit extent no longer depends on the term; it affects prose only. See `08-glossary.md`.
- **Schema coverage of record‑level keys.** Several keys in active use across all records are not yet defined in the schema's `field_definitions`. They are outside the validator's remit, so the gap is documentation debt rather than a validation gap.
- **Census anchor verification against the live scale file.** One class of check can run only when the typographic scale file is present; it currently reports SKIP. The extraction path has not been exercised against the real file.
- **A second global clause registration**, pending the author's adjudication.
- **The typographic realisation of the title sentence** relative to the author's maquette annotations, to be tested against the proof states when those are encoded.

## How to raise one

Open a GitHub issue with the label `open-question`, stating: what is unresolved; whether it is a judgement or a collation; which units or records it touches; and what would settle it. Accepted issues are transcribed into the relevant canonical file with attribution.

Questions about **level‑0 scope** — "should X be recorded at level‑0?" — are especially welcome, and are the questions the project most wants to be argued with about.
