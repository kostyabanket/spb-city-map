# SPB MAP — Agent A architecture source review (2026-11-06)

[Full original report](../reports/2026-11-06-agent-A-architecture-sources.md). **Status: received, unique, archived; primary source-level coverage tests incomplete.**

## Useful differentiated source roles
- GAR/FIAS (https://www.nalog.gov.ru/opendata/7707329152-fias/) — modern **addresses**, XML exports, not historical buildings or physical building identities. Candidate import subject to dataset conditions.
- OSM (https://www.openstreetmap.org/copyright) — building footprints/geospatial topology, ODbL attribution/share-alike concerns. Building footprint coverage for pilot not measured.
- KGIOP/RGIS/EGROKN — heritage designation and legal identity, not universal architectural building corpus. Specific verified registry item IDs not yet obtained.
- Citywalls (https://www.citywalls.ru/) — dates, architect, style and historical narrative, good LINK/REVIEW candidate. Bulk reuse license/API unverified.
- PastVu — pictures and location, belongs also to C's visual sources pipeline; **do not count as an independent architecture-years database**.

## Distinct architectural conclusions
Physical building ≠ address object ≠ plot/parcel ≠ heritage record ≠ architectural complex ≠ building phase. Different stages of construction (e.g. Benois complex) explain apparent year conflicts. Preserve source claims for each specific part. Current `place_id` remains stable, external source IDs mapped separately.

## Missing checks
1. The four documented case studies include **Singer House and New Holland**, not actual pilots `SPB-PET-0001` Двор-восьмиугольник, `SPB-PET-0002` Двор-Бэтмен, `SPB-PET-0003` Дом Трёх Бенуа, `SPB-PET-0011` Дом Лидваля. All four actual place IDs need identity assessment.
2. No concrete XML GAR record with stable ID/normalization and full name for a pilot address, no OSM feature ID/geometry link and no precise official heritage (EGROKN) record for a pilot. Broad source docs != record-level mapping.
3. No demonstrated ground-truth sample coverage/precision; 100-building test is a future proposal only.
4. Confusing source roles risk: GAR cannot validate construction year; OSM geometry does not establish architectural authorship; heritage register does not cover all buildings.
5. No documented legal clearance for mass copying Citywalls or archive-derived images.
6. The twelve opportunity ideas overlap some of B/C/D's entities; deduplicate centrally rather than add as new Sheet columns.
7. Report's claim about additional Lidval address `Кронверкский пр., 15` should not be treated as same building without precise geometry/documentary corroboration.

## Targeted follow-up for Agent A — small evidence table, no new overview
Collect **one row per candidate source record** for all four actual `SPB-PET-0001/0002/0003/0011` and at least two building-specific sources each for Benois and Lidval if possible. Fields: `place_id`, `source`, `source_record_url`, `external_id`, `record_type`, `raw_address`, `normalized_address`, `building_or_complex_or_parcel`, `geometry_or_address_point`, `construction_start/end` (if supported), `architect`, `heritage_designation_id` (if supported), `license_or_terms_url`, `matching_confidence`, `claim_and_justification`, `review_status`.
- Cite at least **one exact GAR/FIAS address record or explain why none accessible**.
- Cite at least **one OSM building feature link** for actual pilot with `way/relation` ID; verify it is the intended building.
- Cite at least **one official KGIOP/EGROKN individual legal record**, if accessible; clarify ensemble vs building, protected property vs physical object.
- For the **two courtyards**, establish containing building(s) or parcel, entrances and safe public access only if evidenced; do not assume every courtyard has its own construction year/architect.
- Show one concrete **year disagreement** and resolve whether it pertains to initial phase vs complex vs secondary source.
- Evaluate 3 pilot-ready importable/linkable facts, with no copyrighted text scraping; provide exact provenance and rights state.
- End with an **up to 10 record** gold sample proposal and 3 no-go conditions.

**Decision:** preserve report and source leads. No automatic import to canonical Sheet, map or publication. Begin record-level crosswalk via small sample and human review.
