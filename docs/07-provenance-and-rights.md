# 07 · Provenance, method, and rights

## Sources

The canonical registry is `data/global/sources.json`. It records every source this
project uses, in three kinds — witnesses, documentary sources, and prior analyses —
with the role each plays and the confidence attached to what was taken from it. What
follows is an orientation, not a second registry: where the two differ, the JSON is
authoritative.

**The base text, and only one.** The Ronat–Papp setting of 1980 — *Un coup de dés
jamais n'abolira le hasard*, édition mise en œuvre et présentée par Mitsou Ronat,
réalisée par Tibor Papp (Paris, Change errant / d'atelier). Every measurement in
level‑0 is a measurement of this object. Where a witness differs, the difference is a
`variant_note` — a lead for the variants layer — and never a reason to alter the
level‑0 record.

**Witnesses** — editions and states in which the text appears, consulted for
comparison and never used as a base: *NRF* 1914, *Cosmopolis* 1897, and the
Firmin‑Didot proofs. The proofs enter this project only indirectly at present; the
registry says so rather than implying direct access.

**Documentary sources** — critical apparatus and commentary: the Pléiade edition of
1998 edited by Bertrand Marchal; the second fascicle of the 1980 edition, in which
Ronat and Papp each set out their own account of what they had done; and Françoise
Morel's facsimile edition of 2007, which reproduces the manuscript and the proofs
themselves.

**Prior analyses** — a third kind, and the reason the registry has three rather than
two. The 1987 hand‑scroll syntactic diagrams are the present editor's own earlier
work on this poem. They are consulted here for segmentation, but they are not a
witness: a witness is a state of the text, and these are an interpretation of it. The
distinction is the same one level‑0 draws everywhere else, applied to the registry.

### The copy that was measured

A bibliographic description names an edition; measurement happens to a copy. Since
every `type_class` in level‑0 records a ruler applied to a particular physical object,
that object is identified here.

The editor's copy of the Ronat–Papp edition is complete, with the second fascicle
present. It carries no serial number. Inside the upper right of the outer frame there
is a pencilled shop annotation. This is the copy that was read for the master's thesis
of 1987 and from which the hand‑scroll diagrams were drawn, and it is the same copy
against which every record in `data/level0/` was collated in 2026 — so the
measurements and the 1987 analysis rest on one object, not on two copies of one
edition.

None of this is a claim about other copies of the edition.

## Method

1. **Transcribe from the photograph of the base copy.** Not from memory, not from another edition, not from general knowledge of the poem.
2. **Collate against the physical copy.** The record's `status` advances to `collated_with_original` only after this step, by the person who performed it.
3. **Assign `type_class` and `style`** from ruler measurement, subordinating photographic estimation.
4. **Run `tools/check_level0.py`.** Structural validation before canonicalisation.

Judgements outside level‑0 scope encountered along the way are written into `note` fields and left there. They are material for later layers, not decisions.

### Two measurement rules with stated reasons

- **Ruler over photograph.** Photographic mm conversion across the gutter runs short by a consistent factor of about 1.10, because the paper recedes from the camera near the fold. Being systematic, the error survives internal consistency checks; only the ruler catches it. Photographic values are retained in pixels as secondary evidence, never converted into canonical millimetres.
- **Approved census over per‑image ratio.** Relative height within a single photograph produced a wrong classification early in the project. Class assignment goes through the census, whose anchors are individually measured occurrences.

### Errors before and after canonicalisation

Drafting errors caught before a record is canonicalised leave no trace in `revision_history`, because that ledger documents changes to the record, not the encoder's path to it. Errors found after canonicalisation are always recorded, with `before`, `after`, `evidence`, and `by`.

## What is not in this repository

**No photographs of the base copy or the witnesses are redistributed here.** The record consists of transcription, measurement, and structural description produced from them.

Consequences to be honest about: some observations cannot be independently re‑verified from this repository alone. Anyone wishing to check them needs access to the same editions. The repository is therefore designed to state its method precisely enough that verification is possible for someone who obtains the copies, rather than to substitute for them.

## Rights

The summary table is in [`RIGHTS.md`](../RIGHTS.md); the scope of the licences, what
they do not cover, and the reasoning behind them are in
[`LICENSING.md`](../LICENSING.md). They are not repeated here, so that there is one
place to correct if any of it changes.

What belongs here rather than there is the connection to method: this repository
publishes measurements and structured records made *from* the objects named above, and
publishes no reproduction *of* them. That is why the section above is careful about
which copy was measured, and why the section below is careful about what could not be
independently re‑verified from this repository alone.

## Acknowledgement of process

Parts of this encoding were drafted in dialogue with AI systems and then verified by the author against the physical copies. Where a draft assertion failed collation, the failure is documented in the project's operating rules rather than concealed — the photograph‑first rule exists precisely because plausible reconstruction from familiarity produced errors three times early on. Machine drafting is treated here as a labour‑saving device subject to human collation, never as a source of evidence. The distinction between drafted and collated states is carried in every record's `status` field, so a reader never has to guess which they are looking at.
