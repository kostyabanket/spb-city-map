# SPB MAP — Integrated Research Synthesis and Pilot Gate v1
**Date:** 2026-11-06. **Status:** research-only planning, no production import or publication.

## 1. Intake complete
All five tracks A–E delivered initial reports; B delivered second edition plus two targeted supplements, A supplied records and a corrected identity table, C supplied 11 media and a confirmed octagon-view follow-up, D supplied five-source feasibility and corrected four-existing-place scope; E delivered 340-field matrix and 33 overlap candidates.

### Primary research
- [A architecture](./reports/2026-11-06-agent-A-architecture-sources.md), [A corrected eight records](./reports/2026-11-06-agent-A-corrected-record-evidence.md)
- [B residents](./reports/2026-11-06-agent-B-people-addresses.md), [B second](./reports/2026-11-06-agent-B-people-addresses-second.md), [B evidence follow-up](./reports/2026-11-06-agent-B-evidence-followup.md), [B archive blockers and corrected Chudov date](./reviews/2026-11-06-agent-B-archive-blockers-and-chudov-correction.md)
- [C historical media](./reports/2026-11-06-agent-C-visual-archives.md), [C 11-asset follow-up](./reports/2026-11-06-agent-C-verified-media-followup.md), [C octagon verification](./reviews/2026-11-06-agent-C-octagon-photo-confirmation.md)
- [D breadth](./reports/2026-11-06-agent-D-opportunity-discovery.md), [D source feasibility](./reports/2026-11-06-agent-D-source-feasibility-followup.md), [D corrected four places](./reports/2026-11-06-agent-D-corrected-four-place-pilot.md)
- [E architecture](./reports/2026-11-06-agent-E-data-architecture.md), [field audit matrix](./data/2026-11-06-agent-E-field-audit-340.csv), [overlap candidates](./data/2026-11-06-agent-E-overlap-candidates.csv)

## 2. Non-negotiable entity identities
**Only four existing map entries**:
- `SPB-PET-0001` — Двор-восьмиугольник, Малый пр. П. С. 1Б; related physical building: Zanin revenue house, address 1б lit. A according to cited 2023 heritage examination.
- `SPB-PET-0002` — Двор-Бэтмен, **Большой пр. П. С. 104**, related Diderichs house. **Rubinshteina 40/11 Ioffe courtyard is a DIFFERENT place**, even if similarly nicknamed Batman/cat.
- `SPB-PET-0003` — Дом трёх Бенуа, Kamenoostrovsky 26–28, multi-part ensemble including historically differently-addressed buildings.
- `SPB-PET-0011` — Дом Лидваля, Kamenoostrovsky 1–3, historically multi-building complex.

**Do not create a SPB MAP `place_id`** for New Holland or Krasny Treugolnik until separate editorial decision.

## 3. Common minimal schema (research side)
- `Entity(entity_id, entity_type, canonical_place_id?, labels)`
- `EntityRelation(subject_id, predicate, object_id, time_range?, match_status)`
- `SourceRecord(source_id, origin_url, archival_locator?, accessed_at, retrieval_status)`
- `Assertion(claim_id, subject_id, predicate, value_original, value_normalized, valid_from?, valid_to?, temporal_precision, review_status)`
- `EvidenceLink(claim_id, source_id, locator, strength, directly_inspected, contradicted_by?)`
- `MediaAsset(asset_id, commons_file_or_pastvu_cid, creator, work_date, rights_url, attribution, depict_match_status, camera_point?)`
- `RightsRecord(source_or_asset_id, reuse_status, assessed_at, conditions)`
- `LegacyProjection(place_id, legacy_35_fields, projection_version)`

The 35 present Sheet headers are **compatibility contract**. All 340 inventory positions retained; 33 E overlap rows are *possible* overlaps, not proven duplicates. **Do not mutate production Sheet, `data/places.geojson`, app or public map**.

## 4. Three bounded pilots to build outside production

### Pilot P1 — Actual four-place identity + licensed media (maximum 4 entity/asset pairs and 10 claims)
**Input:** existing public record IDs/addresses; A's revised candidate building/heritage relationships; C's Commons file-level rights & photographer.
**Candidate photograph for each:**
- `0001` https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg (Ekaterina Borisova, 2017-05-25, CC BY-SA 4.0; upward octagonal opening confirmed by C's visual review, exact camera point unknown).
- `0002` https://commons.wikimedia.org/wiki/File:Двор-колодец_%22Бэтмен%22.jpg (Бегущий из города, 2020-09-18, CC BY-SA 4.0; Diderichs/Bolshoy P.S.104).
- `0003` https://commons.wikimedia.org/wiki/File:BenoisHouse.jpg (Potekhin, 2008-12-30, CC BY-SA 3.0).
- `0011` https://commons.wikimedia.org/wiki/File:LidvalHouse.jpg (Potekhin, 2010-01, CC BY-SA 3.0).
**Acceptance:** real unchanged place IDs; exact file page and license; author and attribution; differentiated place vs containing building vs complex; no wrong Ioffe join; no invented OSM polygon or confirmed GAR GUID; any present rights uncertainty blocks use of that media; no unintended legacy export difference.
**Deliverable:** `research/pilots/p1-four-places-media-candidates.csv`, with explicit source, attribution, match/review status; no image copied or downloaded.

### Pilot P2 — Historic residence/address claim graph (maximum 10 candidate assertions)
**Input:** B's 10 candidates, archive catalogue references and named research. Original scans not directly read; preserve `primary_seen=false`.
**Critical correction:** M. S. Chudov **left** historical address Kronverkskaya 23/59 apartment 40 **in 1930**, `start_year=UNKNOWN`; research says he moved to Kronverkskaya 21 apartment 8. Do not interpret 1930 as move-in to old apartment.
**Acceptance:** owned property != resided at; flat/apartment != entire building; Benois different corps and changing addresses distinct; unknown date bounds explicit; no protected personal information; no publication as primary verified.
**Deliverable:** `research/pilots/p2-person-address-candidates.csv` plus claim/error notes.

### Pilot P3 — Industrial history / typed city entities (maximum 8 claims)
**Input:** D's evidence from TsGA St Petersburg `R-1360` archival fund, annual headcounts, organization `Q112033468`, building complex `Q4239624`. Separate organizations and buildings.
**Accept:** original archive items are catalogued, their actual folios not read; workforce stats dated individually, not automatically comparable; no plan geometry unless plan image accessed; publication rights handled.
**Deliverable:** `research/pilots/p3-industrial-claims-candidates.csv` with `research_only` status, no actual public `place_id`.

## 5. Source roles and rights
- GAR/FIAS — address normalization; some secondary GUID candidates only, **no official extracted row** for pilots.
- OSM — building/site geometry; no directly inspected building way/relation for four actual places; ODbL when used.
- KGIOP/EGROKN — legal protection entity, not identical to building, complex or house ID. Wikivoyage category IDs not official registry numbers.
- Citywalls, regional archives, RNB city directories — provenance/review, no mass copying without licenses and source-specific permissions.
- Commons — CC BY-SA **per asset**, not blanket source license.
- PastVu — documented photo API and historical images; **link only** until actual per-image rights resolved.
- Wikidata — CC0 metadata candidate, source assertions still subject to historical verification.
- GBIF — dataset reference available, **no directly verified occurrence `gbifID` in St Petersburg**; hold ecology pilot.

## 6. Work order and gates
1. Create the three separate offline candidate tables using original references (no new source mass scraping). **Next concrete step**.
2. Cross-check P1's four rows and P2's ten against current legacy 35 fields using read-only exported current records.
3. Check each candidate record `source_url`, `rights`, `source_record_id`, `identity_match`, `review_status` and missing-value semantics; mark UNVERIFIED where necessary.
4. Run an isolated reversible projection/round-trip on a snapshot only, never on the canonical Sheet. Compare four `place_id` values and current GeoJSON content hashes; no publication.
5. Only after user/editorial approval consider any change to canonical Sheets, GeoJSON, app or new entities.

## 7. Who should be asked now?
**No more agent follow-ups required to start the P1–P3 offline data prototype.** A, B, C, D and E all delivered the current bounded tasks; stop the repeated request cycle. If a missing primary document/GIS geometry is required by a later gate, issue one tightly scoped task with expected proof and stop condition. Otherwise coordinator advances to tangible files and QA.
