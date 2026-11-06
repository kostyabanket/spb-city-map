# SPB MAP Research D — review and follow-up (2026-11-06)

Full report: [Research D / 26 concepts](../reports/2026-11-06-agent-D-opportunity-discovery.md). Status: **RECEIVED, SAVED, REVIEWED; SOURCE-LEVEL PILOTS PENDING**.

## Principal value
- Wide-angle source survey covers 13 candidates and 26 concepts; the report explicitly distinguishes 340 existing field headers from new *entities and relations*. This satisfies BREADTH.
- Best distinctive proposals: `Enterprise/Establishment` history and address episodes (historical commerce, industry); `SpatialState/UrbanChangeEvent` historical versions; `LostUrbanObject` predecessor/successor relations; time-varying transit; flood footprints; biodiversity and soundscapes.
- Concrete leads include [SPb official open data](https://data.gov.spb.ru/), [RGIS](https://rgis.spb.ru/), [SPb archives](https://spbarchives.ru/infres), [RNB directory](https://nlr.ru/cont/v_p/), [OSM](https://www.openstreetmap.org/), [Wikidata](https://www.wikidata.org/), [GBIF](https://www.gbif.org/), [iNaturalist](https://www.inaturalist.org/), [Freesound](https://freesound.org/), [Europeana](https://www.europeana.eu/).
- Important case studies: alleged historic bronze/lamp manufacturing predecessor on Lidval parcel; archive fund `Р-1360` industrial transformation of Krasny Treugolnik; historic flood 1824 map in National Electronic Library; 1900s commerce directories.

## Critical corrections and remaining gaps
1. Source-count and topic coverage are **research discovery, not tested API imports**. No dataset-level URL, sample row/schema, publication date, licensing and machine access verified for most official or thematic data.
2. The report again replaces existing pilot courtyards with Krasny Treugolnik and New Holland. Test all four *actual* IDs (two courtyards, Benois, Lidval) or honestly mark untestable.
3. The five highlighted directions are promising, but not all cheap: historical parcel changes, 3-time-slice mapping and lost-city contours depend on maps/permissions and expert georeferencing. Separate a 1-week proof of data from 6-month platform roadmaps.
4. Comparative scoring chart lacks a reproducible table of 26 numeric scores/weights in the uploaded text. Demand a transparent 26-row ranking or remove implied precise ranking.
5. Cross-report source **deduplication**: PastVu/archives/addresses overlap with B and C. New priority leads are OSM spatial entities, Wikidata entity linking, GBIF/iNaturalist biodiversity, Europeana rights-aware metadata, official open-data layers, archive industrial funds.
6. For every outward concept, identify whether it is new `property`, `entity`, `relation`, `temporal state` or `UI experience`, and point at closest current 340 fields.
7. Historical commerce and workers may include living persons, modern occupancy and licensed source content: limit public personal information and record rights gates.
8. Avoid declaring that GIS or portal has a machine-readable layer merely because a map renders it.

## Targeted follow-up
A. Create **five executable source cards**: (1) official SPb open data concrete dataset, (2) OSM small bounding-box map feature, (3) Wikidata example with Q-ID, (4) GBIF/iNaturalist one public urban-nature observation, (5) one archival industrial record. Each: exact item/dataset URL, stable ID, sample fields, coordinate/temporal match, license and API/doc URL, intended SPB MAP entity/field, and realistic join mechanism. If live testing unavailable say so. No mass crawling.
B. Give a **26-row deduplicated opportunity matrix** with `new_object_type`, `existing_field_overlap`, `source_readiness`, `user_value`, `effort`, `licensing_status`, `confidence`, `rank`; include scores + weights if claiming numerical prioritization.
C. Give exactly **three small pilot specifications**: one `DEPTH` improvement to four existing places, one `BREADTH` citywide novel type not centered on buildings, and one cross-domain compound example. Each limited to ≤10 records and no production writes. Define acceptance metrics.
D. Try to find **one real, directly linked historical predecessor** of Lidval parcel and distinguish it from *modern* Lidval house. Provide source quote/precise reference + dates + parcel/address matching evidence; unclear parcel history => `unverified`.
E. For the actual two courtyards `SPB-PET-0001` and `SPB-PET-0002`, outline which wide-angle data families are applicable (address/building membership, morphology, streetscape, historic photos, accessibility, ecological observations) and give evidence where available rather than substituting sites.
F. Provide five **truly new** directions not overlapping the current report's 26 (examples: historical street lighting, public-health urban infrastructure, changing recreational use of watercourses, accessibility at block level, verified community oral history), with likely source class and a reason users would care. Label speculative leads.

## Orchestrator decision
Preserve all 26 ideas in opportunity backlog, but **do not create 26 new Sheet columns**. Source rights/availability + item-level join + pilot success decide implementation priority. Run the first cross-domain data proof on **one or two existing objects**, and use the remaining discoveries for future citywide layers.
