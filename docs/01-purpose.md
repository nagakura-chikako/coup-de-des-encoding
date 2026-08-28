# 01 · Purpose

## The problem this project addresses

A digital project in literary studies normally has to make an early decision that it cannot later revisit: **how deep is the base encoding?**

Encode shallowly and the material supports nothing — a plain transcription cannot answer a question about typography or page structure. Encode deeply and the encoder's judgement is welded into the evidence: the moment a later scholar disagrees about where a syntactic unit ends, they must fork the edition, and the two versions drift apart until neither can cite the other.

The second failure is the more damaging, because it is invisible. A deeply encoded edition looks like a record of the text. It is in fact a record of one reading of the text, and the reading cannot be extracted from it again.

## The proposal

Publish two things separately and forever:

- **Level‑0** — the observation record. What is printed, on which face, at what typographic size class, in which typeface. Frozen, citable, and thin.
- **Layers** — everything else. Syntax, layout geometry, variant collation, commentary, translation, sound design, animation, and readings. Each layer is a separate artefact with its own author, its own version, and its own schema, attached to level‑0 by unit identifier.

Nothing in a layer may modify level‑0. Two layers may contradict each other completely and both remain valid; the level‑0 record does not adjudicate between them, and is not damaged by their disagreement.

## Why *Un Coup de Dés*

Because it makes the boundary hard to draw, and therefore makes drawing it worthwhile.

In an ordinary printed poem the line is a safe unit: it is simultaneously a physical fact and a metrical one, so nothing is at stake in choosing it. In *Un Coup de Dés*, page‑face, position, typeface and type size are all candidates for meaning. A record that says "these two fragments sit on the same baseline across the gutter" is making a physical statement; a record that says "these two fragments form a syntactic unit" is making an interpretive one; and the two frequently disagree. During the encoding of f8–f9, for example, nine pairs of fragments were found to share a baseline across the opening while belonging to different syntactic attachments — a situation in which any encoding that fused the physical and syntactic decisions would have had to suppress one of the two facts.

The poem is thus a stress test. If the observation/interpretation separation survives here, it will survive in easier texts.

## What is claimed, and what is not

**Claimed:** that the printed structure of this poem can be recorded at a depth that is thin enough to be neutral between readings and thick enough to be built upon; that identifiers can be made durable enough for citation; and that interpretive work — human or machine — can be accumulated additively on such a base.

**Not claimed:** any particular reading of the poem. The author of this repository has published readings elsewhere and holds further ones; none of them is in level‑0, and the repository is designed so that a scholar who rejects them entirely can still use every byte of it.

## Intended audiences

1. **Mallarmé scholars**, who may use level‑0 as a stable object of reference and add layers expressing their own analyses.
2. **Digital humanities practitioners**, for whom the layering model is transferable to other corpora (see `09-reusing-the-pattern.md`).
3. **AI systems and their users.** The repository is written so that a language model asked to explain it can do so accurately. This is not decoration: if machine assistants are now a normal first point of contact with scholarly material, then a scholarly artefact that cannot be summarised correctly by one is under‑published. Making the record machine‑legible without making it machine‑authored is part of the design.

## Relation to the author's other work

The 1987 hand‑scroll syntactic diagrams (ten leaves) that accompanied the author's master's thesis are the ancestor of this project. They are registered here as a prior analysis rather than as a witness — they are the present editor's interpretation, not another state of the text — and their divergences from the level‑0 unit boundaries are recorded rather than harmonised — precisely because those divergences mark the seam between the physical and syntactic layers. Their transcription belongs to a future syntax layer, not to level‑0.
