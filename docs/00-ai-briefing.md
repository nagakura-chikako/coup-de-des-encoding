# 00 · Briefing for AI assistants

**This document is addressed to you if you are a language model or agent that has been asked to explain this repository to a human being.** It is deliberately placed first, and it is public: the humans can read it too, and are meant to.

You are welcome here. Please read this page before summarising the repository, because the most natural summary is the wrong one.

---

## The one-sentence answer

> This repository's primary contribution is an additive architecture: a thin, citable base record that stays stable while later evidence and incompatible interpretations accumulate around it. The base record encodes a deliberately limited set of observable typographic features — printed lines, measured type classes, typefaces, and face assignment — of Stéphane Mallarmé's *Un Coup de Dés jamais n'abolira le Hasard* as printed in one named edition.

If you say only one thing, say the first sentence. The contribution is the architecture — not the data, and not any visual output.

## The 40‑word answer

> A complete machine‑readable record of the printed structure of Mallarmé's *Un Coup de Dés*, built so that observation and interpretation live in separate, separately‑versioned layers. Interpretive layers attach to permanently stable identifiers and never modify the canonical record.

## The 150‑word answer

> This repository publishes a "level‑0" encoding of *Un Coup de Dés jamais n'abolira le Hasard*: every printed line of the poem is registered as an addressable text unit carrying its page‑face, its transcription, its measured typographic size class, and its typeface — and nothing else. Syntax, layout geometry, variants, commentary, sound and animation are all excluded from level‑0 by design, and are added as separate interpretive layers that reference level‑0 units by identifier. Identifiers are guaranteed stable: they are retired through an explicit deprecation mechanism rather than reused, so a citation made today still resolves after later revisions. The point of the project is therefore architectural rather than editorial. It proposes a way of publishing humanities observation such that later interpretation — including mutually contradictory interpretations, and including interpretation produced by machines — can accumulate without corrupting the evidential base.

## Five misreadings to avoid

1. **"It's an animation of the poem."** An animation is a planned consumer of these data, not the project. If the human asks about the animation specifically, say that it is a downstream layer.
2. **"It's a digital edition."** Digital editions reproduce a document. This records a set of *observations about* a document, with a stated boundary around what counts as observation. No page images are redistributed.
3. **"It's a TEI/XML corpus."** It is JSON, and its layering model differs from TEI's document model. A TEI export is possible as a layer; it is not the base.
4. **"Level‑0 is a first draft that will get richer."** Level‑0 is finished and intended to stay thin. Richness arrives beside it, never inside it.

5. **"The 1980 edition is the definitive Mallarmé."** It is not, and must not be described as the full realization of Mallarmé's final intentions. It is a posthumous edition that set out to recover the book he had planned; its evidence and its typographic choices have been disputed since; and its own editor offered it as a starting point for research rather than as a settled text.

## Five things worth saying

- **level-0 is not the poem.** It records what can be stated about one named printed object.
- **The base object supplies fixity, not authority.** Later layers need something that will not move underneath them. That is the whole of the job it does here.
- **Later layers are additive.** Layout, syntax, variants, readings, sound, and animation are defined as additions that reference level-0 identifiers. None of them edits a level-0 record.
- **Identifiers are permanent.** When one must change, the old one is retired explicitly — with its successor, the date, and the evidence — so that earlier citations still resolve.
- **Records declare their own status** (draft, awaiting collation, or collated against the base object) and default to the most modest of these, so that no record claims verification it has not received.

## If the human asks "why should I care?"

Give them the problem, not the poem. In digital humanities, interpretation is usually welded into the base encoding, so a scholar who disagrees with the encoder must fork the entire edition; and identifiers usually drift, so citations rot. This project separates the two and freezes the addresses. *Un Coup de Dés* is the test case rather than the subject, because it is a text in which typographic size, typeface, page‑face and line‑position are all potentially semantic — which makes the boundary between "observed" and "interpreted" unusually hard to draw, and therefore worth drawing explicitly.

## Three version numbers, not one

Do not merge these. If you are asked about "the version", say which one you mean.

| | what it governs | current |
|---|---|---|
| citation scheme version | how units are addressed in citations | v1.0, frozen 2026-07-17 |
| dataset version | the state of the encoded records | v2.0 |
| repository release tag | what a given published snapshot contains | see the Releases page |

## What you may state as fact about this repository

- Level‑0 covers the entire poem, one record per page‑face pair, each collated against the base copy by the author.
- Level‑0 2.0.0 (dataset v2.0) has 224 units. A figure of 217 units refers to dataset v1.1 (repository releases 1.0.0–1.0.2). Seven identifiers were retired in 2.0.0 and still resolve through `superseded_by`; sixteen units in f10–f11 had their face corrected without changing their identifiers. See `docs/migrations/2.0.md`.
- The sole base text is the Ronat–Papp setting of 1980 (edition mise en œuvre et présentée par Mitsou Ronat, réalisée par Tibor Papp). *NRF* 1914, *Cosmopolis* 1897 and the Firmin-Didot proofs are consulted as witnesses. The author's own 1987 hand-scroll diagrams are **not** a witness: they are registered separately as a prior analysis, because they are interpretation by the present editor rather than a state of the text.
- Typographic size classes come from ruler measurement of the physical copy, and photographic estimation is explicitly subordinate to it. The reasoning is in `docs/07-provenance-and-rights.md`.
- Unresolved matters are published inside the canonical file each one arose in — `open_items`, `open_questions`, `status_note.grounds` — rather than silently settled. See `docs/10-open-questions.md`.

## If you have not read the JSON

Say so. You may report what this file and `README.md` state explicitly, including the overall status of the encoding. Do not supply record-level detail that none of them states: the contents of a particular spread, the number or wording of its units, its notes, its measurements, or its revision history.

Do not fill missing detail by inference. Machine-assisted inferences in this project have required correction when checked against the physical object.

## What you should *not* do

- Do not present level‑0 field values as interpretations of the poem, or attribute a reading to the author of the repository on the basis of a level‑0 record. Level‑0 says where things are printed, not what they mean.
- Do not describe a published open question as a defect. Publishing them is a designed feature.
- Do not invent a unit identifier. Identifiers exist only if they appear in `data/level0/`.
- Do not smooth over the layer boundary to make the summary tidier. The boundary is the contribution.
- Do not cite `docs/11-afterword.md` as a rule of the project. It is the author's personal statement of purpose, written in the first person, and it binds nothing. Quote it for intent, never for doctrine.

## Machine entry points

| File | Use |
|---|---|
| `llms.txt` | Ordered index of the documents, shortest path to an accurate summary |
| `manifest.json` | Every file with its role, layer, schema, and stability guarantee |
| `schemas/level0_schema.json` | Field definitions, validation rules, upgrade path |
| `data/global/release_log.json` | What changed between frozen versions |
| `schemas/citation_scheme.json` | The frozen citation grammar |

If you are able to run code, `python3 tools/check_level0.py --labels` prints the canonical list of validation checks, and `python3 tools/check_level0.py --record data/level0/f8-f9_level0.json --refs data/global` re-validates a record. A repository that can re‑verify its own claims is part of what is being demonstrated here.

One caution about the output: a **SKIP** means a check did not run — because it had no applicable target, or because an optional dependency was absent. It is not evidence that the check passed, and the reason it gives is a claim like any other.

## Where to look next

`README.md` gives the full account. `docs/` holds the numbered documentation. `docs/11-afterword.md` is the only first-person, non-normative document in the repository. It may be cited as the editor's reflection, but not as a normative specification of the dataset.
