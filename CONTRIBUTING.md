# Contributing

A Japanese version of this file is at [`CONTRIBUTING.ja.md`](CONTRIBUTING.ja.md).

Contributions are welcome. Please read [`README.md`](README.md) first — this document assumes the layer model it describes.

## How contributions are accepted right now

**Issues, not pull requests.** Pull requests are not being accepted at present. Please open an issue instead.

The reason is specific to this project rather than a general policy. A correction to level-0 is not settled by being merged; it is settled through direct inspection of the physical base object and, where relevant, measurement. In this project, merging would record an agreement that has not yet taken place. And the layers above level-0 do not exist yet, so there is as yet no stable shape for a contribution to fit into.

This will be revisited once the first layer above level-0 is in place. Until then, an issue is not a lesser form of contribution here. It is the form this record is built to hold: dated, attributed, carrying its evidence, and preserved whether or not it is acted on.

You are also free to fork this repository and work in your own copy, under the terms in [`LICENSE`](LICENSE). Nothing here is intended to keep the material out of anyone's hands.

By opening an issue, you agree that the material in it may be incorporated into this repository under the licences already in force here — CC BY 4.0 for records, schemas and prose, MIT for `tools/` — with attribution as described in [`LICENSING.md`](LICENSING.md). This adds no condition beyond those licences, and it leaves your own rights in your own work untouched.

Issues are reviewed. Not every issue will receive an individual reply, and a reply may take some time — but an issue is preserved and remains readable whether or not it is answered.

## The one rule

**Additions, not rewrites.** Every contribution either adds something new or records a change; nothing is corrected by silently replacing it. A citation made ten years from now should still resolve to something.

This is not a matter of etiquette. It is what makes the base record usable as a common reference at all.

## Three kinds of contribution

All three arrive as issues.

**1. Corrections to a level-0 record.** The bar is high, because level-0 claims only what is physically observable on one named object. A correction here means one of two things: the record misstates what is on the page, or an identifier must be retired. Both require evidence (see below).

**2. Additions in a later layer.** Layout, syntax, variants, readings, sound, proof states, and the typographic maquette all live above level-0 and reference its identifiers. This is where most substantive work belongs — including work that contradicts the project editor's own published readings. A later layer may disagree with anything except the physical record.

**3. Notes, disagreements, and questions.** If you think something is wrong but cannot yet prove it, say so. Open questions are a normal part of the record here, not a defect in it.

## What a correction must carry

- **What changed** — the field, and its value before and after.
- **The evidence** — what you looked at, and how. "The 1914 printing reads otherwise" is a comparison, not evidence about the base object.
- **The date, and who made it** — a person or a machine. If a language model, a script, or an OCR pass produced the reading, say so plainly. This is not held against the contribution; it is part of what a reader needs in order to weigh it.

Identifier changes additionally go through `deprecated_ids`, naming the successor identifier so that earlier citations continue to resolve. A unit recorded on the wrong face is not an identifier change: the face is corrected in `revision_history` and the identifier stays.

## Who can certify collation

A record's `status` says how far it has actually been checked, and the strongest value — collated against the base object — means someone compared the record to the physical copy in front of them, including measuring the type.

**Opening an issue does not by itself raise a record's status.** You may propose a correction from a photograph, a scan, or a reproduction, and it will be recorded as such. A status may be raised only after collation against a physical copy of the base object has been verified and incorporated into the canonical record. The base object was printed in a small edition, so if you hold a copy of your own, please identify it as far as you can. Not every copy carries a serial number, so use whatever actually identifies yours: a holding institution and shelfmark, a bookseller's label, a purchase record, an ownership stamp, a pencilled annotation. Copies may differ in trimming and in paper.

This asymmetry is deliberate. Most of the corrections already in the record history exist because something inferred from an image turned out to be wrong when a ruler was applied to paper.

## Disagreement

Incompatible readings are expected, and are not resolved by deletion. If your reading contradicts one already recorded, the outcome is that both are recorded, each with its evidence and its author. The architecture exists to hold disagreement, not to arbitrate it.

The one thing that is arbitrated is the physical record. If two people disagree about what is printed on the page, that is a question with an answer, and the answer is sought by direct inspection of the base object and, where relevant, by measurement.

## Ordinary repository maintenance

Nothing above prevents the maintainer from removing spam, mistaken uploads, duplicated files, broken data, or material that has to be taken down for legal or privacy reasons. "Additions, not rewrites" is a rule about the scholarly record, not a promise to keep everything ever submitted.

## Practically

- **One spread, or one question, per issue.** Records are organized by spread, and issues spanning many at once are hard to check.
- **Say what you actually looked at** — the base object, a photograph, another printing, a reproduction, or the JSON alone. This matters more than being right.
- **Quote the identifier**, not just the words. `tu_…` identifiers are stable; wording alone is ambiguous across printings.
- **An issue template is provided** for corrections. It asks for the identifier, what changed, the evidence, and what you examined. Using it is the fastest route.
- **Running the checker is welcome but not required**: `python3 tools/check_level0.py --record data/level0/<record>.json --refs data/global`. It reports PASS / FAIL / SKIP, and a SKIP is not a failure — it means the check does not apply, or that an optional input was not supplied.
