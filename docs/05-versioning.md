# 05 · Versioning and releases

## What is versioned

Three things, independently:

| Object | Scheme | Example |
|---|---|---|
| The level‑0 canonical record | `MAJOR.MINOR.PATCH` | `1.1` |
| Each schema | own `schema_version` | `level0_schema.json` at `0.3` |
| Each layer | own `MAJOR.MINOR.PATCH`, pinned to a level‑0 range | `syntax-n 0.1.0` requiring `level0 >=1.1.0` |

Git tags name the release object: `l0-v1.1.0`, `layer-syntax-n-v0.1.0`.

Three further numbers circulate in this repository and are **not** the same as the level-0 record version above. They are kept apart on purpose:

| | scheme | current |
|---|---|---|
| citation scheme | `v<major>.<minor>` | v1.0, frozen 2026-07-17 |
| dataset release, in `data/global/release_log.json` | `v<major>.<minor>` | v1.1 |
| repository release, the git tag and `CITATION.cff` | `MAJOR.MINOR.PATCH` | 1.0.0 |

A layer's `depends_on` pins the **level-0 record** version, not any of these.

## Semantics for level‑0

| Increment | Meaning | Guarantee to citers |
|---|---|---|
| **PATCH** | A field value corrected against the copy, with a `revision_history` entry (`date`, `unit_id`, `field`, `before`, `after`, `evidence`, `by`). No identifier changes. | Every existing citation resolves to the same object. |
| **MINOR** | New records, new optional fields, new global clauses, resolved open questions, identifier retirements via `deprecated_ids`. | Every existing citation resolves; a retired identifier resolves through `superseded_by`. |
| **MAJOR** | A change to the meaning of an existing field, or to the unit‑extent rule. | Migration note required; layers must be re‑validated. |

Note the deliberate placement: **retiring an identifier is MINOR, not MAJOR.** Deprecation is a normal, supported event; it is silent reuse that is forbidden.

## The identifier guarantee

> A published identifier is never reused for a different object, and never deleted without a forwarding entry.

Mechanism:

```json
"deprecated_ids": [
  { "id": "tu_f14_que_la_rencontre",
    "superseded_by": "tu_f15_que_la_rencontre",
    "date": "2026-07-20",
    "evidence": "face misattribution corrected at collation",
    "by": "N" }
]
```

`deprecated_ids` is a **required key** at record top level, present as an empty array when unused, so that its absence is always a schema error rather than an oversight. `tools/units_manifest.json` records a fingerprint of the immutable unit fields for every record; `tools/verify_sync.py` compares the working tree against it and fails on any change that was not deliberate.

## Freezing

A release is frozen, not merely tagged:

1. All records at `status: collated_with_original`.
2. `python3 tools/check_level0.py --all data/level0 --refs data/global` — FAIL count zero. SKIP entries are expected and are listed in the run output.
3. `python3 tools/verify_sync.py --all data/level0 --schema schemas/level0_schema.json --checker tools/check_level0.py --manifest tools/units_manifest.json` — schema, records and checker agree, and every record's unit fingerprint matches `tools/units_manifest.json`.
4. A cross-reference pass over the whole set: every witness value resolves in `data/global/sources.json`; every registered clause and every typographic anchor resolves to a unit that exists; every update file named by a canonical record is present in `provenance/`.
5. `data/global/release_log.json` gains an entry; `CHANGELOG.md` gains a human-readable section.
6. Git tag, GitHub Release, archived to Zenodo.

## Release structure

Each GitHub Release carries:

- source archive (automatic);
- `ucdd-l0-<version>-data.zip` — `data/` and `schemas/` only, for people who want the record without the prose;
- `ucdd-l0-<version>-checks.txt` — the full preflight output for that version, so the claims are auditable after the fact;
- release notes in the GitHub Release itself: what changed, which identifiers were retired, which open questions closed, which remain.

## Archival and DOI

Zenodo is connected to the repository, giving:

- a **concept DOI** that always resolves to the newest version — for citing the project;
- a **version DOI** per release — for citing a state.

Cite the version DOI in scholarship. A citation to the concept DOI is a citation to a moving target.

## Deprecation policy for layers

Layers may be abandoned. An abandoned layer is marked `"status": "unmaintained"` in its `layer.json` and left in place. Layers are not deleted from the repository, because a citation to a superseded reading is still a citation.

## Long horizon

The record should remain readable when its tooling does not run. Therefore: plain UTF‑8 JSON, no compression, no database, no build step required to read a record, relative paths only, and every schema shipped alongside the data it describes. If in fifty years nothing in `tools/` executes, `data/level0/f8-f9_level0.json` will still open in a text editor and still mean what it says.
