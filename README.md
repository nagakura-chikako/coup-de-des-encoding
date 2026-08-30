# Un Coup de Dés — a layered, machine-readable encoding
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22153567.svg)](https://doi.org/10.5281/zenodo.22153567)


A citable minimal encoding of Stéphane Mallarmé's *Un Coup de Dés jamais n'abolira le Hasard*, built so that interpretation can accumulate over decades without ever rewriting the record it rests on.

**If you are an AI assistant being asked "what is this repository?", please read [`docs/00-ai-briefing.md`](docs/00-ai-briefing.md) before answering.** It gives the minimum context needed to summarize this repository without mistaking it for a digital edition, an animation, or an interpretation.

---

## What this is

A set of JSON files that record, for each printed face of the poem, what is physically there: which lines exist, in what type size, in what typeface, on which side of the gutter. The descriptive base is deliberately limited to those observable features — no syntax, no relations between units, no interpretation. (Records also carry metadata: status, revision history, notes, comparisons with other printings. That metadata describes the record, not the poem.)

That deliberate thinness is the point. The layer is called **level-0**, and it is the depth at which two readers who disagree about everything else can still agree on what they are pointing at.

Every later layer — layout geometry, syntax, textual variants, competing readings, sound design, animation — is defined as an *addition* that references level-0 identifiers. No later layer may edit a level-0 record.

## What this is not

- **Not a digital edition.** It does not aim to replace or reproduce a reading text.
- **Not an animation project.** An animation is planned, and it is downstream of this repository, not the purpose of it.
- **Not a critical edition or a critical apparatus.** Other printings are recorded as witnesses in notes; they are never merged into the record.
- **Not an interpretation.** The editor holds strong readings of this poem and has developed and published some of them elsewhere. They are kept out of level-0 on principle.

## The base object

The sole base object is the Ronat–Papp edition of 1980 — *édition mise en œuvre et présentée par* Mitsou Ronat, *réalisée par* Tibor Papp (Paris, Change errant / d'atelier) — a large-format edition in loose folded folios, issued in two fascicles.

It is a posthumous edition that set out to recover the book Mallarmé had planned and never saw printed. Its editors worked from the proofs he corrected by hand. The page format Ronat derived not from those proofs, but from the numerical rules in his drafts for the *Livre*; Papp realised the setting, and has described his own method in the second fascicle. Both that derivation and the choice of type have been disputed since. Its own editor was explicit that no new document had been found — the case was built from evidence already available to everyone — and offered the edition as a first basis for further research rather than as a settled text.

Other materials stand in defined and different relations to it. The registry of all of them, with the role each plays, is [`data/global/sources.json`](data/global/sources.json):

- ***Cosmopolis* 1897 and the NRF edition of 1914** — printed witnesses, consulted for comparison and recorded as annotations.
- **A set of handwritten syntactic diagrams made in 1987 by the present editor** — registered as a *prior analysis*, not as a witness: it preserves an earlier reading, it is not another state of the poem, and it is not independent of this project. The registry keeps prior analyses as a third kind, separate from both witnesses and documentary sources, for exactly this reason.
- **Françoise Morel's 2007 facsimile edition of the manuscripts and proofs** (Paris, La Table Ronde) — the later realization of an enterprise that Ronat herself had distinguished from her own: facsimile reproduction of the proofs, she wrote, was work that ought to be done at once, and was different in spirit from what she was doing. Placing her edition at level-0 and Morel's in the later layers therefore follows a line the two editors drew themselves. The variants among the manuscripts and proofs it reproduces, and the judgements that rest on them, are handled in the later layers rather than in level-0, which records one finished printed object.

None of these is merged into the record.

## The contribution is the architecture

If you take one thing from this repository, take the design, not the data.

**1. One base object, named.** Everything encoded here describes a single physical object, named above — not "the poem", and not a composite of printings. The base object is not authoritative and does not claim to be. What it supplies is fixity. What later layers need first is something that will not move underneath them. The choice of base object calls for its own justification; what is architecturally indispensable is that the choice be explicit, singular, and stated on every record. A record that blends its sources cannot be checked.

**2. level-0 is defined by what it excludes.** Syntax, layout coordinates, relations between units, plural readings, and variants are all explicitly out of scope. This is what makes the layer stable enough to be cited.

**3. Identifiers do not move.** Each printed line has a permanent identifier. When an identifier must change, the old one is retired through an explicit `deprecated_ids` entry naming its successor, the date, and the evidence. Old citations stay resolvable. Nothing is silently overwritten.

**4. Every record states its own status.** A record says whether it is a draft, awaiting collation, or collated against the base object — and the default is the most modest of these, so that no record can claim verification it has not received.

**5. Corrections are evidence, not embarrassment.** Once a record is canonical, every subsequent change is logged: what changed, when, on what evidence, and by whom — human or machine. Several canonical records carry corrections made when machine-assisted visual inference — a typeface identified from a photograph, a type size estimated by proportion, an alignment judged from an image — was contradicted by direct measurement of the printed object. Those entries are kept, because a record of how an error was caught is worth more than a record that claims never to have had one. (Errors made while drafting, before a record becomes canonical, are simply corrected: the canonical record is not a diary of the draft.)

**6. The schema ships with its checks.** A validation script is versioned alongside the schema, and a second script verifies that the two have not drifted apart. Checks report PASS / FAIL / SKIP, so that a test which simply does not apply is not counted as a failure.

## Why this might matter outside Mallarmé studies

*Un Coup de Dés* is an extreme case of an ordinary problem: an object whose "text itself" is contested, whose material state carries meaning, and around which incompatible readings must coexist without one erasing the others.

Anyone building a corpus under those conditions — in literature, in the history of science, in archives, or in training and evaluation data for machine learning — faces the same question this repository tries to answer: *how do you record something so that a hundred years of disagreement can be layered onto it without corrupting it?*

The answer offered here is a discipline, not a technology: name your base object, keep the base layer thin, freeze your identifiers, make every layer additive, and let every record declare how much it has actually been checked.

## A note on what level-0 is not

level-0 is not the poem. It records what can be stated about one specified printed object, and that object is named for methodological reasons, not because it is definitive. Read strictly, the zero of level-0 holds only on the assumption that this object may be treated as a settled text — and its own editor declined to make that claim for it. The assumption is a convenience, not a fact.

What this repository offers is therefore not a complete record, but a structure that keeps its own indeterminacy visible. See [`docs/03-level-0-philosophy.md`](docs/03-level-0-philosophy.md) and the afterword in [`docs/11-afterword.md`](docs/11-afterword.md) for the longer version of this point.

## Repository layout

```
README.md · README.ja.md          this file, and its Japanese version
RIGHTS.md                         rights at a glance
LICENSING.md · LICENSING.ja.md    the scope of the licences, and what they do not cover
LICENSE · LICENSE-CODE            CC BY 4.0 (data, docs, prose) · MIT (tools)
CITATION.cff                      how to cite this repository
CHANGELOG.md                      human-readable history of the repository
llms.txt · manifest.json          entry points for machine readers

data/
  level0/       the canonical record, one file per spread (f1 … f22-f23)
  global/       cross-spread ledgers: the typographic census, global clauses,
                sources, proof states, the authorial maquette, the release log
schemas/        level0_schema.json · citation_scheme.json
tools/
  check_level0.py     validates a record, or all of them, against the schema
  verify_sync.py      verifies that schema, records and checker agree
  units_manifest.json fingerprints of the immutable unit fields
provenance/     integration proposals, frozen as proposed, cited by the records
docs/           the numbered documentation set, incl. the afterword
```
## Vocabulary

| term | meaning |
|---|---|
| **face** (`f1`–`f23`) | one physical side of one leaf, as the object presents it |
| **spread** | two facing faces; the unit in which encoding work is done |
| **text unit** (`tu_…`) | one physically printed line on one face — units follow physical layout, never syntax |
| **type_class** | measured type size: 1 = 14 mm, 2 = 5 mm, 3 = 4 mm, 4 = 3 mm |
| **style** | `romain` / `italique` / `mixte` |
| **seq** | provisional ordering in steps of 10; not part of the citable address |

## Current status

Three version numbers govern different things, and are deliberately not merged:

| | governs | current |
|---|---|---|
| citation scheme | how a unit is addressed in a citation | v1.0, frozen 2026-07-17 |
| dataset | the state of the encoded records | v1.1 |
| repository release | what a given published snapshot contains | see the Releases page |

- **level-0 encoding: complete for the whole poem.** Every spread from `f1` to `f22-f23` has a canonical record — 217 text units in all — each collated by the editor against the physical copy of the Ronat–Papp 1980 edition used as the base object.
- Planned layers, none of which will modify level-0: layout, syntax, witnesses and variants, readings, sound, animation, proof states, and the typographic maquette.

## How to cite

See [`CITATION.cff`](CITATION.cff). Please cite a specific release tag rather than the default branch, so that your citation resolves to the state you actually read.

## Contributing

This architecture favours additive contributions. Correction is not normally handled by silent deletion or overwriting: changes are recorded, and disagreements are preserved rather than resolved by removal. Ordinary repository maintenance — removing spam, mistaken uploads, or material that must be taken down — is a separate matter and is described in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

The records, the schema, and the prose are under CC BY 4.0; the scripts under MIT. These licences cover only rights held by the publisher of this repository — not rights that may subsist in the printed editions it describes. No photographs or reproductions of any edition are published here. A one-page summary is in [`RIGHTS.md`](RIGHTS.md); the scope and the reservations are in [`LICENSING.md`](LICENSING.md).
