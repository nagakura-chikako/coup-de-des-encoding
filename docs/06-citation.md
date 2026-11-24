# 06 · Citation

## Citing the project

> Nagakura, Chikako. *Un Coup de Dés — Layered Canonical Encoding (UCDD‑L0)*, release 2.0.0 (dataset v2.0), 2026. Zenodo. DOI: 10.5281/zenodo.22153567

That DOI is the concept DOI and always resolves to the newest version. To cite the state you read, use the version DOI shown on the Zenodo page of release 2.0.0.

Machine‑readable equivalents: `CITATION.cff` (GitHub renders a "Cite this repository" button from it) and the `citation` block of `manifest.json`.

## Citing a single unit

The address form is the one defined in `schemas/citation_scheme.json`, frozen on 2026‑07‑17:

```
ucd[:<release>]://<address>[@<selectors>]
ucd:v2.0://unit/tu_f8_le_maitre
```

`<release>` is the dataset release. Omit it only for a deliberately moving reference; scholarly citations should pin it.

Optionally qualified by depth:

```
ucd:v2.0://unit/tu_f8_le_maitre@depth=level-0
```

The `@depth` selector matters because the same identifier will later be addressed by layers. `@depth=level-0` says: I am citing the observation, not any reading attached to it.

What is deliberately **not** part of the address:

- `seq`. It is a convenience ordering and would smuggle a claim of linearity into every citation.
- File paths. Records may be reorganised; identifiers may not.

## Citing a spread record

```
ucd:v2.0://spread/f8-f9
```

## Citing a layer claim

A claim in a layer is cited through the unit it attaches to, with the `@layer` selector, and `@rev` for a fixed revision of that claim:

```
ucd:v2.0://unit/tu_f6_par@layer=N;rev=1
```

The dataset release and the layer both appear, because a layer claim is only meaningful relative to the record it attaches to.

## In prose

> Level‑0 records `par` (f6) and `avance retombée d'un mal à dresser le vol` (f7) as two units on a shared baseline (ucd:v2.0://unit/tu_f6_par, ucd:v2.0://unit/tu_f7_avance_retombee); their reading as a single phrase belongs to a layer (ucd:v2.0://unit/tu_f6_par@layer=N).

The form is verbose on purpose. It makes visible, in the citation itself, where observation stops and interpretation starts.

## Citing a retired identifier

If a cited identifier appears in a `deprecated_ids` entry, the citation remains valid and resolves through `superseded_by`. Nothing needs to be withdrawn. Later work should cite the current identifier and may note the retirement. Where a unit was split, `superseded_by` lists two successors; cite the one your argument concerns, or both.

A unit whose face was corrected keeps its identifier, so there is nothing to resolve. The correction is in that record's `revision_history`.

## Resolving a citation without tooling

1. Find the version in `CHANGELOG.md` or on the Releases page and download that release. (Dataset v1.1 is repository release 1.0.2; dataset v2.0 is 2.0.0.)
2. Grep the identifier in `data/level0/`.
3. If absent, grep it in the `deprecated_ids` arrays and follow `superseded_by`.

Three steps, no service, no server, no dependency on this repository's continued hosting.

## Requested practice

If you build on this record, please cite the version DOI rather than the repository URL, and please state which layers, if any, your argument depends on. The second request is the more important one: an argument that depends on a syntax layer is a different kind of claim from one that depends only on level‑0, and readers are entitled to know which they are being offered.
