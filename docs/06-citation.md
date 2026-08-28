# 06 · Citation

## Citing the project

> Nagakura, Chikako. *Un Coup de Dés — Layered Canonical Encoding (UCDD‑L0)*, release v1.1, 2026. DOI: assigned at first release (Zenodo)

Machine‑readable equivalents: `CITATION.cff` (GitHub renders a "Cite this repository" button from it) and the `citation` block of `manifest.json`.

## Citing a single unit

The canonical address form is:

```
UCDD-L0/<version>#<unit_id>
UCDD-L0/1.1#tu_f8_le_maitre
```

Optionally qualified by depth, which is what `schemas/citation_scheme.json` encodes:

```
UCDD-L0/1.1#tu_f8_le_maitre@level-0
```

The `@depth` selector matters because the same identifier will later be addressed by layers. `@level-0` says: I am citing the observation, not any reading attached to it.

What is deliberately **not** part of the address:

- `seq`. It is a convenience ordering and would smuggle a claim of linearity into every citation.
- File paths. Records may be reorganised; identifiers may not.

## Citing a spread record

```
UCDD-L0/1.1#f8-f9
```

## Citing a layer claim

```
UCDD-L0/1.1 + layer:syntax-n/0.1.0#syn_n_f6_par_avance
```

The level‑0 version and the layer version both appear, because a layer claim is only meaningful relative to the record it attaches to.

## In prose

> Level‑0 records `par` (f6) and `avance retombée d'un mal à dresser le vol` (f7) as two units on a shared baseline (UCDD‑L0/1.1#tu_f6_par, #tu_f7_avance_retombee); their reading as a single phrase is asserted in the syntax layer (layer:syntax‑n/0.1.0#syn_n_f6_par_avance).

The form is verbose on purpose. It makes visible, in the citation itself, where observation stops and interpretation starts.

## Citing a retired identifier

If a cited identifier appears in a `deprecated_ids` entry, the citation remains valid and resolves through `superseded_by`. Nothing needs to be withdrawn. Later work should cite the current identifier and may note the retirement.

## Resolving a citation without tooling

1. Find the version in `CHANGELOG.md` or on the Releases page and download that release.
2. Grep the identifier in `data/level0/`.
3. If absent, grep it in the `deprecated_ids` arrays and follow `superseded_by`.

Three steps, no service, no server, no dependency on this repository's continued hosting.

## Requested practice

If you build on this record, please cite the version DOI rather than the repository URL, and please state which layers, if any, your argument depends on. The second request is the more important one: an argument that depends on a syntax layer is a different kind of claim from one that depends only on level‑0, and readers are entitled to know which they are being offered.
