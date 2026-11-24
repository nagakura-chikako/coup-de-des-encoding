# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning semantics for level-0 are defined in [docs/05-versioning.md](docs/05-versioning.md).

Headings name the dataset version; the date is the day that version passed its final check. The repository release that published it is named under each heading; its publication date is on the Releases page and in `CITATION.cff`.

## [2.0] — 2026-11-24 — repository release 2.0.0

Level-0 2.0.0. **MAJOR**: the unit-extent rule for lines that cross the gutter is replaced. Migration note: [docs/migrations/2.0.md](docs/migrations/2.0.md).

### Changed
- Lines crossing the gutter are recorded as one unit per face, whether the spread is one sheet or two. Seven units split (f12–f13: 4; f16–f17: 3); 217 → 224 units.
- Schema 0.3 → 0.4: `id_assignment_rules[1]` replaced; `superseded_by` may list several successors; a face correction keeps the identifier and is recorded in `revision_history`.
- Validator: check 3 accepts a mismatch between an identifier's face prefix and its face only when the face corrections form an unbroken chain; check 21 added (retired identifiers resolve, are not duplicated, do not remain in `units`).

### Fixed
- f10–f11: sixteen units (`tu_f11_celui` … `tu_f11_folie`) are printed on f10, not f11. Face corrected, identifiers kept (ruled 2026-09-26, collated 2026-11-24).
- f6–f7: the blank between `par` and `avance retombée…` is 8 cm by ruler, not the ≈67 mm converted from the photograph.
- `typography_scale.json`: the proposed class-3 italic anchor follows the split to `tu_f12_une_insinuation`.
- Documentation: version numbers and unit counts; citation examples now use the frozen `ucd:` form; the unused `l0-v…` tag convention is described as such.

### Retired identifiers
`tu_f12_une_insinuation_simple`, `tu_f12_au_silence_enroulee`, `tu_f12_dans_quelque_proche_tourbillon`, `tu_f12_voltige_autour_du_gouffre`, `tu_f16_la_lucide_et_seigneuriale_aigrette`, `tu_f16_une_stature_mignonne_tenebreuse`, `tu_f16_par_d_impatientes_squames_ultimes` — each resolves to two successors through `superseded_by`.

## [1.1] — 2026-08-28 — first public release

Published as repository releases 1.0.0 (2026-08-28), 1.0.1 (2026-08-29, `CITATION.cff` adjusted for the Zenodo importer) and 1.0.2 (2026-09-02, documentation fixes; data unchanged).

### Added
- Complete level-0 coverage of the poem: f1, f2-f3, f4-f5, f6-f7, f8-f9, f10-f11, f12-f13, f14-f15, f16-f17, f18-f19, f20-f21, f22-f23. All records at `status: collated_with_original`.
- Public reference documentation, `docs/00`–`docs/11`.
- `llms.txt` and `manifest.json` for machine readers.
- `tools/check_level0.py`, `tools/verify_sync.py`, and `tools/units_manifest.json`: a validator, a schema/checker sync check, and a fingerprint ledger of the immutable unit fields.
- Layer template and contribution rules.

### Notes
- Typographic scale established as canonical v0.3: four measured size classes (14 / 5 / 4 / 3 mm), class-first organisation, separate paratext clause, measurement log.
- Validator outcomes are three-valued (PASS / FAIL / SKIP); a SKIP means a check did not run, not that it passed.

## [1.0] — 2026-07-17

### Added
- Citation scheme frozen; release log opened.
