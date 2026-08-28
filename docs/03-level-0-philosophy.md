# 03 · The level‑0 philosophy

## Definition

> **Level‑0 is the minimum depth at which citability is guaranteed.**

Not the minimum depth that is useful, and not the maximum depth that is defensible. The minimum depth at which one can point at something and be certain that the same thing will be found there later, by someone who disagrees with everything else in the project.

## The three questions used to admit or exclude a field

A candidate field enters level‑0 only if it passes all three.

1. **Could two competent scholars who disagree about the poem's meaning still agree on this value?**
   *Type size passes.* A syntactic bracket does not.
2. **Is the value established by an act of observation whose method can be stated?**
   Ruler, photograph, eye, collation against the copy. If the answer is "by reading it carefully", the field belongs to a layer.
3. **Would removing it make an existing citation unresolvable?**
   If not, it can wait. Level‑0 fails toward thinness.

## What is excluded, and why the exclusions are the substance

The following are **deliberately absent** from level‑0. Each exclusion was contested during construction, and each was decided against inclusion:

| Excluded | Why |
|---|---|
| Syntactic units and relations | The most valuable thing the project has to offer, and therefore the most dangerous to freeze. A syntax layer can be replaced; a syntax‑contaminated base cannot. |
| Layout geometry (coordinates, margins, whitespace) | Measurable, but only within a coordinate frame that is itself a modelling decision. Belongs to a layout layer with its own declared frame. |
| Variant collation | Witness comparison is an argument, not an observation. Divergences noticed during work are parked in `variant_notes` as leads, not as collation. |
| Readings and commentary | By definition. |
| Prosody, sound, animation | Downstream consumers. |
| The hand‑scroll annotations, verbatim | Their transcription is a task for the syntax layer. Level‑0 records only their location and their divergences from the unit boundaries. |

Reading that table is the fastest way to understand what the project is: **level‑0 is defined by what it refuses.**

## The unit boundary rule, and the case that established it

Level‑0 unit extent is decided by physical layout, not by sense.

The rule was tested on f6–f7. The word `par` sits at the foot of f6 and `avance retombée d'un mal à dresser le vol` at the head of f7, and the two share a single baseline to within about 0.15 mm — but with roughly 67 mm of blank between them, some twenty‑five word‑spaces. Physically: two units, on two faces. Readably: plainly one phrase, and the 1987 hand‑scroll had treated it as one. The decision was to keep two units at level‑0 and to state that `par avance` may be read as a unit in the syntax and readings layers.

That decision looks like pedantry and is in fact the entire design. Had the units been fused, the record would have asserted a reading — a persuasive one, but a reading — and the physical separation would have become unrecoverable. Keeping them apart costs one note and preserves both facts.

The same pattern recurs: `sauf que` across f14–f15, `l'évènement` / `accompli` across f20–f21, `endroit` / `fusionne` across f22–f23. In each case level‑0 splits by face and a layer joins.

## Observation is not raw

The project does not claim that level‑0 is theory‑free. It claims something weaker and more useful: that the *method* by which each value was obtained is stated, and that the values were checked against the physical copy rather than against memory or general knowledge of the poem.

That precaution is empirical. Three separate drafting errors early in the project — an image confusion at f1, a phantom two‑line offset at f2–f3, a misread line division at f4–f5 — all had the same cause: a plausible reconstruction from prior familiarity with the poem, arriving before the photograph was consulted. Hence the operating rule, stated in the schema and enforced in review: **the photograph and the copy come first; nothing is filled in from memory.** Drafting‑stage errors caught before canonicalisation are not recorded in `revision_history`, since the record documents the state of the text, not the state of the encoder.

## What "canonical" means here

That the record is frozen at a version, collated against the base copy, and addressable. It does **not** mean infallible. It means that if it is wrong, the correction will be visible: a `revision_history` entry with `before`, `after`, `evidence` and `by`, or — where identity itself changes — a deprecation with `superseded_by`.

The zero is provisional in a further sense. It is a zero only relative to a single printed state — one reconstructed after the poet's death, and final only by accident. It is the smallest fiction under which reference becomes possible, not a floor the poem itself provides.

A canonical record is not one that cannot be wrong. It is one that cannot be wrong quietly.

## Why open questions are published

Open questions are carried inside the canonical file each one arose in, in two kinds of entry distinguished by field rather than tone:

- `status: open` — a design judgement still to be made.
- `category: pending_verbatim_collation` — a matter that will be settled by checking the copy, no judgement required.

Publishing them costs the appearance of completeness and buys the thing that matters: a reader can tell the difference between what has been decided and what has merely not been raised. An edition with no open questions is not finished; it is silent.
