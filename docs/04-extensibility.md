# 04 · Extensibility — how to add a layer without touching the canonical record

## The contract

1. A layer lives in its own directory under `layers/`.
2. A layer references level‑0 by identifier. It never copies level‑0 field values as its own assertions, and never edits `data/`.
3. A layer declares the level‑0 version it was built against.
4. A layer is signed. Every claim belongs to someone.
5. Layers do not depend on each other unless they declare it. Two layers of the same kind may coexist and contradict.

If a layer cannot be expressed without changing level‑0, that is a finding, and it should be filed as an open question rather than worked around. So far it has happened zero times; the interesting cases (`par avance`, `sauf que`, `l'évènement / accompli`) were all expressible as layer‑side joins.

## Minimal layer

```
layers/syntax-n/
  layer.json          declaration (see below)
  README.md           what this layer claims, in prose, for humans
  annotations/
    f8-f9.json      entries referencing tu_* identifiers
```

`layer.json`:

```json
{
  "layer_id": "syntax-n",
  "title": "Syntactic segmentation after the 1987 hand-scroll diagrams",
  "version": "0.1.0",
  "depends_on": { "level0": ">=2.0.0" },
  "authors": [{ "name": "Nagakura Chikako", "sigla": "N" }],
  "claim_type": "interpretive",
  "attaches_to": "text_unit",
  "may_modify_level0": false,
  "license": "CC-BY-4.0"
}
```

An annotation entry:

```json
{
  "annotation_id": "syn_n_f6_par_avance",
  "targets": ["tu_f6_par", "tu_f7_avance_retombee"],
  "relation": "forms_phrase",
  "claim": "par avance is read as a single adverbial phrase separated across the opening.",
  "confidence": "asserted",
  "sigla": "N",
  "date": "2026-07-27",
  "supersedes": null
}
```

`confidence` takes one of `asserted` | `proposed` | `speculative`. `supersedes` carries the `annotation_id` of an entry this one replaces, or `null`: it is the field through which the append-only rule is actually kept, since superseding means adding an entry that points at the old one rather than editing the old one.

Note what the entry does *not* do: it does not delete the two units, does not renumber anything, and does not require the syntax reader and the physical reader to agree.

## Layer kinds already anticipated

| Layer | Attaches to | Notes |
|---|---|---|
| `layout` | text_unit | Coordinates in a declared frame; must state its origin, units, and photographic source. Gutter‑crossing distances belong here, with the systematic photographic shortening documented. |
| `syntax` | text_unit, multi‑unit | Segmentation, case frames, global clauses. Several rival syntax layers are expected. |
| `variants` | text_unit | Witness collation (*Cosmopolis*, *NRF*, typescript, proofs). Currently leads are parked in level‑0 `variant_notes`; the layer converts leads into collation. |
| `readings` | anything | Interpretive commentary. Explicitly permitted to leave the poem — other works, letters, drafts, biography. |
| `handscroll` | text_unit | Verbatim transcription of the 1987 marginalia, with its own divergence table. |
| `sound` | face, style | e.g. the roman/italic page distinction as a sonic parameter. |
| `animation` | anything | Camera, timing, foregrounding events. Consumes level‑0 + layout + syntax. |
| `tei` | record | Export view for interoperability. A *view*, not a second canonical record. |
| `translation` | text_unit | Any language, any number. |

None of these is required for the repository to be complete. Level‑0 is complete now.

## Versioning across the boundary

- A layer pins the level‑0 version it was validated against.
- A level‑0 PATCH (a corrected transcription) does not break layers; the identifier still resolves.
- A level‑0 MINOR (a new field, a new record) does not break layers.
- A level‑0 MAJOR is the only event that may break layers, and it must ship a migration note. Retiring an identifier is *not* a MAJOR change, because `deprecated_ids` + `superseded_by` gives layers a mechanical path forward.

`tools/verify_sync.py` exists so that this promise is checked by a program rather than by good intentions.

## Contributing a layer

Layers may be contributed by anyone, including by machines with a named operator. The contribution rule is **append‑only**: entries are added, never overwritten or deleted, and every entry records who added it and when. There is no gatekeeper approving claims, because the permanence of the record is itself the constraint — a wrong claim stays attached to its author. Superseding an entry means adding a new entry that points at the old one, not editing the old one.

Practical procedure in `CONTRIBUTING.md`.

## For future maintainers

If this repository outlives its author, the guarantee that must be preserved is exactly one sentence long:

> **A published level‑0 identifier never comes to mean something different.**

Everything else in the design can be renegotiated. That cannot.
