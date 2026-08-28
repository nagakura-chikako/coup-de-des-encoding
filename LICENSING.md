# Licensing and rights

日本語版は [`LICENSING.ja.md`](LICENSING.ja.md) にあります。

A one-page summary of the same information is in [`RIGHTS.md`](RIGHTS.md); the sources and the method behind the records are in [`docs/07-provenance-and-rights.md`](docs/07-provenance-and-rights.md). This file is the scope and the reservation.

Two licences apply, according to what a file is.

| | licence | file |
|---|---|---|
| the encoded records, the schema, and all prose — `data/`, `docs/`, `README`, and this file | Creative Commons Attribution 4.0 International (CC BY 4.0) | [`LICENSE`](LICENSE) |
| the scripts — `tools/` | MIT | [`LICENSE-CODE`](LICENSE-CODE) |
| an interpretive layer — `layers/` | declared by the layer itself in its `layer.json`; CC BY 4.0 where none is declared | the layer's own `layer.json` |

CC BY 4.0 permits sharing, adaptation, and commercial use, on condition that credit is given and changes are indicated. It does not require derivative work to carry the same licence. That is deliberate: this repository exists so that others can build layers on top of it, and a share-alike condition would make some of those layers harder to combine with work licensed differently.

## What these licences do not cover

**They apply only to rights held by the publisher of this repository.** They grant nothing in respect of rights that may be held by others.

In particular, this repository describes the typographic setting of a specific printed object: the Ronat–Papp edition of *Un Coup de Dés jamais n'abolira le Hasard* (édition mise en œuvre et présentée par Mitsou Ronat, réalisée par Tibor Papp; Paris, Change errant / d'atelier, 1980). The poem itself is in the public domain. Rights that may subsist in the editorial and typographic arrangement of a modern edition are a separate matter, they vary between jurisdictions, and nothing here is a licence to them or a statement that none exists.

The same applies to every other object named in this repository, including the *Cosmopolis* printing of 1897, the NRF edition of 1914, and Françoise Morel's facsimile edition of 2007. They are described and cited; they are not licensed here.

If you intend to reproduce any of those objects, rather than to reuse this repository's records of them, that permission has to come from elsewhere.

## What this repository publishes

Measurements, identifiers, structured records, a schema, validation scripts, and prose. **No photographs or reproductions of any edition are included.**

That is a decision, not an oversight. The records are checkable without images: anyone with a copy of the base object can measure it and compare. Publishing images would raise a separate question about reproducing a modern edition, and would also blur the point the repository makes about itself — that it is not a digital edition and offers nothing to read in place of the poem.

## Attribution and the author's name

Under CC BY 4.0, credit is due when the records are reused. [`CITATION.cff`](CITATION.cff) gives the preferred form.

This work is authored by **Chikako Nagakura**, the name under which the author's scholarly work on Mallarmé has been published. Chikako Nakayama is the author's current legal name and is used in the author's professional work in music and opera. Please cite this repository under Nagakura, so that it stays connected to the rest of that body of scholarship.

Please cite a specific release tag rather than the default branch, so that the citation resolves to the state that was actually read.
