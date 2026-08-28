# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning semantics for level-0 are defined in [docs/05-versioning.md](docs/05-versioning.md).

## [1.1] — 2026-XX-XX — first public release

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
