# Research C — review and targeted follow-up (2026-11-06)

Full report: [Agent C visual archive report](./reports/2026-11-06-agent-C-visual-archives.md). Status: **RECEIVED, REVIEWED, REQUIRES PIVOTAL EVIDENCE**.

## Confirmed independently by orchestrator
- [PastVu API documentation](https://docs.pastvu.com/dev/api) confirms `photo.giveForPage`, `photo.giveNearestPhotos`, `photo.getByBounds` and new host `https://api.pastvu.com/api2`; nearest search `[lat,lon]`, GeoJSON bounds `[lon,lat]`. API access is *not* blanket republication permission.
- [Commons reuse guidance](https://commons.wikimedia.org/wiki/Commons:REUSE) requires *per-file* rights, attribution and suitability assessment; displayed license metadata is not a legal warranty.

## Candidate sources for source registry (provisional, not ingestion approvals)
| Source | URL | SPB MAP applicability | Decision |
|---|---|---|---|
| PastVu | https://pastvu.com/ / https://docs.pastvu.com/dev/api | historical_*, links_207, image discovery | LINK / REVIEW; API and image reuse conditions not fully audited |
| Wikimedia Commons | https://commons.wikimedia.org/ | photos_*, historical_*, licensing | SELECTIVE IMPORT after file-by-file license verification |
| ЦГАКФФД | https://spbarchives.ru/web/group/cgakffd | historical attribution and catalog evidence | LINK / REVIEW |
| Library of Congress | https://www.loc.gov/maps/ | historical maps; some API and IIIF | LINK / pilot conditional on item rights |
| Presidential Library | https://www.prlib.ru/ | maps, postcards, archival references | LINK / REVIEW; item-level copy restrictions |
| РГАКФД | https://photo.rgakfd.ru/ | historical image provenance | REVIEW |
| РНБ | https://nlr.ru/poisk/ | cartographic/bibliographic research | LINK |
| Net-Film | https://www.net-film.ru/ | footage catalog | LINK / license review |
| Retromap | https://retromap.ru/ | historic cartography | INVESTIGATE |
| ЭтоРетро | https://etoretro.ru/ | user-submitted historical photographs | REVIEW |

## New potential entity types — not new Sheet columns by default
`VisualAsset`, `VisualWork`, `ArchiveRecord`, `CameraPose`, `DepictedObject`, `RightsProfile`, `ThenNowPair`, `HistoricalMapLayer`, `VideoGeospatialSegment`, `VisualEvidenceClaim`. Keep original photo ID vs derived scans and distinguish scene coordinates vs camera position.

## Key gaps before implementation
1. The agent's four spot checks included **Palace Square and Nevsky Prospekt instead of existing pilot courtyards**. Required actual IDs: `SPB-PET-0001` Двор-восьмиугольник, `SPB-PET-0002` Двор-Бэтмен, `SPB-PET-0003` Дом Трёх Бенуа, `SPB-PET-0011` Дом Лидваля. Need URL-level matching for all four, including `not found`.
2. Report mostly cites collections and category homepages, not a **catalog item with verified identifier, concrete metadata, direct rights statement and whether it actually depicts the intended building**.
3. PastVu API methods documented, but **no live bounded call/result, error behavior, rate limit, API ToS or per-photo usage permissions** were established.
4. A claimed photo from a related street or nearby building is **not automatically a record about the exact place**. Visual match and role (main/background/ambiguous) required.
5. Score 4.3/5 etc. are expert estimates with no reproducible criterion-by-criterion evidence. Do not turn into objective rankings.
6. Distinguish copyright in original historical work, rights in reproduction/scanned copy, database/API contractual conditions and thumbnail embedding.
7. Historical view comparison needs **actual two compatible photo records, dated and licensed**, not only a proposed schema.
8. Widening: identify **non-obvious archives** such as ground-level photo documentation of courtyards, architects' drawings, early aerial photography, demolished buildings, industrial visual records, and user-contributed images; avoid duplicates in current field atlas.

## Requested follow-up from Agent C (separate focused deliverable)
A. Make an **evidence table with 4 rows × up to 3 concrete media records**, one section per *actual* pilot `place_id`; cite exact catalog item URLs, IDs, caption, date or date range, exact depicted location, scene coordinates vs camera coordinates, rights/attribution and reliable mapping status. Mark unknowns explicitly. Do not claim missing resources absent evidence.
B. Show **one real PastVu query/response** centered on Lidval building, using safe small limit (<=5), clearly distinguish unrelated nearby images; disclose if unable to call live API. Include response `cid`, URL and year, not file binaries. No bulk download.
C. Show **one specific Wikimedia Commons file** for Lidval or Benois, with file description link, author, license URL, attribution text, potential modifiers, and justified import-vs-link choice. Do not copy any media.
D. Investigate PastVu policies for automated access: rate limits, robots/terms, rights to save metadata/thumbnails, attribution; give direct policy links and say *unverified* where absent.
E. Expand outward with **5 new visual discovery opportunities** particularly for courtyards, hidden architectural details, lost or unbuilt places and repeat photography; cross-check against existing 340 fields.
F. End with a single **one-week small pilot specification**: input columns, output records, success/fail criteria, exact permissions gate. No Google Sheet or GitHub writes.

## Orchestrator decision
Proceed first with **link-only, proof-based visual catalog for one existing building** once item identity verified. No full-resolution copying or API-powered publication until licensing/ToS is understood. Reserve then-and-now overlay as a separate second-stage experiment.
