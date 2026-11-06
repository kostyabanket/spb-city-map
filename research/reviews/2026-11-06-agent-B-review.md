# SPB MAP Research B — orchestrator review (2026-11-06)

**Status:** report received, archived, methodological findings accepted, direct extraction NOT verified.
Full report: [Agent B source report](../reports/2026-11-06-agent-B-people-addresses.md).

## Main actionable findings
- Address books **«Весь Петербург»** (digital [1903 example](https://rusneb.ru/catalog/000200_000018_v19_rc_1266006/)) and **«Весь Ленинград»** are potential year-by-year person/address mentions; one listing is NOT proof of continuous residence.
- [SPb State Archives](https://spbarchives.ru/infres/-/archive/cga/pointers): registry/pointers of house books, source for targeted validation, not proven mass-open data.
- [Encyclopedia of St Petersburg](https://www.encspb.ru/), museums and municipal libraries: qualified secondary biographical statements, not unrestricted reuse.
- [Wikidata](https://query.wikidata.org/): identifier linking and metadata (CC0), NOT automatically primary evidence of residence.
- Building episodes from report: [Lidval 1903–1918](https://dates.pr-cbs.ru/persons/lidval/) is a secondary claim; [Kirov in apartment 20 of Benois 1926–1934](https://spbmuseum.ru/exhibits_and_exhibitions/permanent_displays/1323/) museum secondary claim; neither yet tied in report to an independently retrieved primary archival page.
- Core distinction: **resident vs owner vs tenant vs visitor vs neighbor**. Person identity confidence and historical claim confidence must be independent.
- Valuable proposed graph entities: `Person`, `ResidenceEpisode`, `PersonPlaceRelation`, `HistoricalAddressVersion`, `EvidenceAssertion`, plus sources per assertion.
- Preserve original writing, historical street names/numbering, publication year, page number, date precision, conflicts, and exact relation type.

## Gap analysis against orchestration spec
1. **Pilot substitution:** agent B worked on Lidval, Benois, Dostoevsky (Kuznechny 5/2), Pushkin (Moyka 12), instead of both actual courtyards `SPB-PET-0001` Octagonal courtyard and `SPB-PET-0002` Batman courtyard. Need actual four-place evidence matrix, including when no residents findable.
2. **Primary evidence gap:** no concrete page/scan with a person/address mention from `Весь Петербург` or `Весь Ленинград` extracted and independently transcribed. Catalog availability != a tested extraction pipeline.
3. **Identity resolution gap:** a worked pair of historical address forms, current building identifier, and potential ambiguity is needed; do not infer direct identity just from the modern address.
4. **Coverage gap:** famous people vs ordinary residents/occupants (source bias), year range, coverage of courtyards where building identity is unclear, households and tenants vs proprietors.
5. **Rights/automation gap:** download ZIP in NEB is not a mass-harvest license; find actual source-specific permission terms, response format and downloadable pages if permissible, and cite them.
6. **Privacy and ethical handling:** do not import potentially living persons' household/occupancy information into public map; develop minimum historical/public-figure rule and manual review.
7. **Reproducibility:** expert source score 4.4/5 not evidence-based coverage measurement; replace or supplement with small measured coverage on actual pilot.
8. **Breadth:** needs more than schema entities: suggest new user-facing questions and new sources for **non-famous city residents**, migrant/occupational communities and changing street names without overstating evidence.

## Focused follow-up for Agent B
A. **All four real SPB MAP objects:** `SPB-PET-0001` Двор-восьмиугольник, `SPB-PET-0002` Двор-Бэтмен, `SPB-PET-0003` Дом Трёх Бенуа, `SPB-PET-0011` Дом Лидваля. Table includes current/known historical addresses, matches and uncertainty, primary/secondary evidence, and `not found/not checked` as appropriate. Courtyards are not residential units: locate **containing building or courtyard complex** first, without inventing residents.
B. **One REAL scanned page of `Весь Петербург` 1903 or comparable year** showing a person's name and specific address relevant to a pilot if possible. Give exact catalog ID, volume/year, page or scan index, original spelling, transcription with context, publication date vs period, persistent URL, and access/licensing. If unsuccessful show obstacles; do not create names.
C. **One independently attributable primary example for Benois/Kirov or Lidval** (may be archival metadata with fond/opis/delo/list; say if original not viewed). Distinguish two secondary pages from truly independent records.
D. **Test a concrete address normalization:** historical street label, historical house number/period, modern address and exact SPB MAP place_id, degree of confidence and alternative hypotheses; one example with multiple Benois buildings.
E. **Data shape:** propose 3 small machine-readable example objects `Person`, `RelationEpisode`, `EvidenceAssertion`, including source-page citation, precision, publisher and status; avoid inventing production IDs.
F. **New beyond 340 fields:** 5 new meaningful types of city investigations, not just more columns; measure benefit, data availability, ethics, distinctness vs existing fields.
G. **One-week micro-pilot:** <=10 real evidence records, no bulk OCR and no live Sheet edits; measurable correctness checks (page-linked entries, ambiguous matches, false-positive residence), licensing/privacy gate.

## Integration decision
Do not automate mass ingestion of resident data yet. First create a **small evidence-only linked-record prototype** for verified historical claims, with permanent page citations and editorial review; no publication of sensitive or current occupancy data.
