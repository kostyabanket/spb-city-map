# SPB MAP — Research E review (2026-11-06)

**Status: UNIQUE / RECEIVED / ARCHIVED / FIRST-PASS AUDITED.**

Files:
- [Architecture report](../reports/2026-11-06-agent-E-data-architecture.md)
- [All 340 field rows](../data/2026-11-06-agent-E-field-audit-340.csv) — 340 records, 19 headers, entirely provisional semantics.
- [Overlap candidates](../data/2026-11-06-agent-E-overlap-candidates.csv) — 33 pairwise candidate rows, **not 33 confirmed full duplicates**.

## Important findings
- 340 headers do not correspond to 340 independent scalar attributes of a building. These include relational data about people, media asset licenses, routes, personal/private user notes and schema/editorial metadata.
- Existing `tools/sheet_to_geojson.py` relies on Russian field names and publication gate; preserve all 35 core headers and legacy behavior as a read-only projection.
- Promising pilot architecture: entities + typed relations + atomized claims + independent evidence and source records + review decisions + publication decisions; no immediate requirement for graph database.
- Preserve original claims and contradictory source versions. `Verification` and `Publication` are separate state machines.
- One meaningful structural distinction: `Период строительства` vs `chronology_022` and `chronology_023` is an aggregation relation, not a proven duplicate.
- Biggest direct candidate duplicate tests: `place_id` / `identity_001`, `Название` / `identity_003`, `Адрес` / `identity_011`, `Архитектурный стиль` / `architecture_037`, `Статус публикации` / `governance_296`.

## Audit cautions / action before schema changes
1. The 340-row table is **mostly generated from header-name heuristics**; inspect value types individually before implementation. In particular, first row `place_id` currently assigned provisional `LocalizedText / controlled vocabulary`, whereas a stable string identifier contract is more appropriate; this is a counterexample to auto-accepting the matrix.
2. The 33 candidate pairwise rows do not establish true equality or migration safety; count distinct candidate pairs and validate actual values from the sole canonical Sheet.
3. Read actual populated `Единая база` values and code consumers, not just headings. Review which supplementary fields are empty, multi-valued, or incorrectly scoped; measure before any removal.
4. Integrate A-D: each proposed source must map to **real current fields AND** additional typed object/relation hypotheses. Preserve rights and original citation/locator.
5. Personal fields have a separate privacy domain. Heritage legal objects must not be conflated with buildings; courtyard != residential building.
6. Keep unchanged all published GeoJSON IDs, current map, canonical sheet and editorial states. No migration or mass data import authorized.

## Recommended focused Agent E follow-up
1. Make the first 35 field types **non-heuristic and exact** (including `place_id`, lat/long, publication/review states, photo rights and URLs), cross-verified with `tools/sheet_to_geojson.py` and 4 actual records.
2. Produce **10 strongest overlapping pairs** from 33 candidate rows, with actual cell values from four rows (if access permitted), explicit same/aggregation/related/not duplicate verdict, and reversible mapping. If Sheets access is unavailable, state lack and give test script/procedure, not a fabricated verdict.
3. Create a single small **JSON Schema for source, claim, evidence and relationship** with distinctions `value_time`, `source_published_at`, `recorded_at`; include 1 truly sourced historical claim and 1 synthetic conflict example; implement no app changes.
4. Show one compatibility test comparing current 4 places `SPB-PET-0001/0002/0003/0011` before and after mock projection; report pass/fail criteria, don't claim test passed unless executed.
5. Explain privacy boundaries and source-rights fields and editorial publication gates concretely.

## Orchestrator decision
**Five of five primary tracks now received.** Next task is *integrated* cross-report Source Registry + Field Atlas + Opportunity Atlas, with first 3 bounded pilots. Stop generating fresh high-level essays; gather item-level primary evidence and test record matching.
