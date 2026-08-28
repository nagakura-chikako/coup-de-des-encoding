# 02 · Architecture

## Overview

```
                    ┌─────────────────────────────────────────┐
   layers/          │  syntax · layout · variants · notes ·    │   additive
   (interpretation) │  readings · sound · animation · TEI …    │   independently versioned
                    └───────────────────┬─────────────────────┘   never edited by others
                                        │ references by unit id
                                        ▼
                    ┌─────────────────────────────────────────┐
   data/level0/     │  one record per spread · text units ·    │   canonical
   (observation)    │  face · text · type_class · style        │   frozen · citable
                    └───────────────────┬─────────────────────┘
                                        │ measured against
                                        ▼
                    ┌─────────────────────────────────────────┐
   physical source  │  base text (Ronat–Papp 1980) · witnesses ·    │   not redistributed
                    │  ruler measurement · photographs         │
                    └─────────────────────────────────────────┘
```

The single rule that generates the whole design: **an arrow may point downward, never upward.** A layer may read level‑0; level‑0 may not read a layer.

## The four object types

### 1. Face

A physical page‑face, `f1` … `f23`. The face is the anchor of physical reality in the model: a unit belongs to exactly one face, always. Where a syntactic phrase crosses a page boundary, level‑0 splits it by face and records the fact in a note; the joining is a syntax‑layer act.

### 2. Text unit

The addressable atom, `tu_<face>_<slug>`. Its extent is decided by **physical layout on the face**, not by readability or sense. A unit carries:

| Field | Content | Kind |
|---|---|---|
| `id` | stable identifier | address |
| `face` | `f8` etc. | observation |
| `text` | transcription, capitalisation preserved, U+2019 for apostrophe | observation |
| `type_class` | integer 1–4 (14 / 5 / 4 / 3 mm), or `null` for paratext outside the census | observation |
| `style` | `romain` / `italique` / `mixte` | observation |
| `seq` | provisional linearisation, in steps of 10 | convenience, **not part of the address** |
| `note` | scoped remark, including out‑of‑scope observations parked for later layers | annotation |

`seq` deserves emphasis: it exists so that tools can iterate in a defined order, and it carries no claim that the poem is linear. It is excluded from the canonical address for exactly that reason.

### 3. Spread record

One JSON file per opening (`data/level0/f8-f9_level0.json`), containing the units of both faces plus record‑level apparatus: `status`, `record_depth`, `evidence`, `physical_observations`, `collation_with_handscroll`, `variant_notes`, `open_questions`, `deprecated_ids`, `revision_history`, `provenance_note`.

`status` has an enum whose default is deliberately pessimistic — `draft_awaiting_collation` — because a template is copied at the start of drafting, and a default of "collated with the original" would silently assert work that had not been done. **Defaults must fail toward under‑claiming.**

### 4. Global ledger

Cross‑spread material in `data/global/`: the typographic size census with its measured anchors, global clause registrations, and the release log. Ledgers are append‑oriented: entries are resolved, not deleted.

## The typographic census

Size classes are not read off photographs. They come from ruler measurement of the physical copy, and the census records, for each class, one or more **anchors** — a specific measured occurrence with its date and measurer. Rules:

- Ruler measurement outranks photographic estimation. This is not fastidiousness: photographic mm conversion across the gutter runs about 10 % short, consistently, because the paper falls away from the camera near the fold. The distortion is systematic, so it fools sanity checks.
- The approved census outranks per‑photograph ratio estimates. An early record classified a spread by apparent relative height and was wrong; the rule dates from that failure.
- Census anchors are drawn from the poem body only. Paratext elements that happen to match a class may carry the class but are registered in a separate `paratext_sizes` clause rather than promoted to anchors.

## Validation

Three programs, all runnable by anyone:

| Tool | Guarantees |
|---|---|
| `tools/check_level0.py` | Per‑record structural validation, PASS / FAIL / **SKIP** three‑valued. Checks with no applicable target, and checks whose optional dependency file is absent, report SKIP and leave the pass/fail denominator. An absent optional dependency must not look like a defect. |
| `tools/verify_sync.py` | Asserts that the checker's label constants and the schema's `machine_checks` list are identical, in order. Documentation that can drift from the code it describes is worse than none. |
| `tools/units_manifest.json` | A fingerprint ledger of the immutable unit fields (id, face, seq, text, type_class, style) for every record. `verify_sync.py` compares the working tree against it and fails on any change that was not deliberate. This is the mechanical enforcement of the citation guarantee. |

The two programs and the ledger are run together before every release; their combined output is the preflight. The repository can therefore re-prove the property it claims, by anyone, at any time, without a service.

## Layer contract

A layer directory contains a `layer.json` declaring:

```json
{
  "layer_id": "syntax",
  "version": "0.1.0",
  "depends_on": { "level0": ">=1.1.0" },
  "authors": [{ "name": "…", "sigla": "N" }],
  "claim_type": "interpretive",
  "attaches_to": "text_unit",
  "may_modify_level0": false
}
```

and any number of annotation files whose entries reference level‑0 identifiers. The interpreter sigla in use (C = Cohn, D = Davies, M = Marchal, K = Kristeva, G = Favre/Garnier, N = Nagakura) are a layer‑level property: a claim is always someone's.

Full rules: `04-extensibility.md`. Template: `layers/_template/`.

## Consequences of the design worth stating plainly

- **Disagreement is cheap.** Two syntax layers may partition the same units differently and both ship.
- **Errors are localised.** A mistake in a layer is a mistake in one file, with a named author and a version.
- **The base can be re‑used by people who reject the project's premises entirely**, which is the strongest test of whether the separation is real.
- **The cost is redundancy.** A fact that "obviously" belongs together — a phrase split across a page boundary — is recorded twice, once split in level‑0 and once joined in a layer. This is accepted deliberately.
