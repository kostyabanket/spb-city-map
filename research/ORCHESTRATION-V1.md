# SPB MAP — Research Orchestration v1 (2026-11-06)

## Goal
Build a **St Petersburg urban knowledge hub**, not merely a map. Two mandatory directions are equal:
- **DEPTH:** map existing 340 canonical Sheet headers to reliable address-linked source data.
- **BREADTH:** propose useful **new field families, city datasets and discovery experiences** missing from the current 340 columns.

Single source of current field names: [field-inventory-340.csv](./field-inventory-340.csv), transcribed read-only from the sole canonical tab `Единая база`. 35 core fields + 305 catalog fields in 18 existing named groups. **Do not change the Sheet, add tabs, publish data, or crawl sites in bulk** as part of research.

## Shared handoff format (every assistant)
Each source candidate must have:
1. Source name, canonical entry URL, owner/publisher and updated/accessed dates if established;
2. What it covers and SPB geography, estimated or verified records (clearly label);
3. Which **exact existing field headers / codes** can be supplied;
4. Additional **new field ideas** (BREADTH), with a clear reason a user would value them;
5. Address/identifier matching (historical address, building vs parcel, duplicates, geolocation confidence);
6. Programmatic availability (documented API, download, structured page, manual link only, unknown);
7. Copyright/licensing/ToS/robots and permitted reuse; label `not verified` rather than assume permission;
8. Source reliability, contradiction risk, and how a claim can be linked to evidence;
9. Test against pilot places `SPB-PET-0001`, `0002`, `0003`, `0011` when practical, distinguishing found/not found/not checked;
10. Recommended handling: `IMPORT`, `LINK`, `REVIEW`, `REJECT`, `INVESTIGATE`, with rationale.

Each assistant must provide a **top-five shortlist** (not hundreds of links), plus a concise `new capabilities` section of at least five ideas (including ideas outside its own main category); cite direct source pages. **Never fabricate source coverage or API permissions.**

## Parallel assignments
### A — Architecture, chronology, geography, use
Fields: `identity_*`, `chronology_*`, `architecture_*`, `usage_*`; pilot `Период строительства`, `Архитектурный стиль`, architect, renovations, former use. Identify canonical address resolution. Compare architectural directories, monument registries, city GIS and open data. Propose new topics such as demolition history, industrial functions, urban planning layers, material/repair eras.

### B — Residents, owners, episodes, culture
Fields: `people_*`, `events_*`, `culture_*`, `legends_*`. Source books, directories, libraries, municipal archives, museum collections. Differentiate historical residents from visitors, owners and notable neighbors, include year and address evidence. Propose new topics such as occupations, professional networks, local associations and street-level microhistories.

### C — Images, archives, video, routes and access
Fields: `photos_*`, `historical_*`, `links_*`, `discover_*`, `access_*`, `routes_*`, `surroundings_*`. Find stable metadata and licensed media; never assume historical images are public domain, never equate API availability to rights clearance. Propose new experiences such as then/now, viewpoint matching, time sliders, accessibility and sensory walks.

### D — Lateral discovery and technical ecosystem
**Do not restrict yourself to 340 fields.** Survey St Petersburg existing local digital city data products, archives, public-sector datasets, volunteering/community catalogs, geographic knowledge graphs and integration techniques. Pitch at least 20 **new useful field types/experiences** grouped by impact and feasibility; compare 10 sources; identify what the project can link to vs ingest; flag source ecosystem gaps, data updates and responsible collection. Then trim to top five experiments. Include at least 5 ideas that are **not building-specific** (parks, courtyards, monuments, public art, routes etc.).

### E — Field registry and evidence architecture
Read all rows in `field-inventory-340.csv`; identify exact vs partial duplicate fields, `core` vs catalog roles, atomic vs multi-valued fields, place-specific applicability, canonical fields and reference-only fields. Draft proposed typed schema **without editing the Sheet**. Design claim-level provenance, confidence and conflict handling, source-to-field mapping, and safe export gates. Include proposals to accommodate discoveries from D without unbounded new physical columns.

## Scoring, not just collecting
Score each proposed source from 0 to 5 in:
`relevance × coverage × traceability × reuse rights × integration feasibility`.
A single 0 in legally permitted reuse => no auto-import; retain a link if allowed.
Distinguish linkability from machine-readability and republishing rights.
Three modes: `import with evidence`, `editor-reviewed summary`, `link-out`.

## Pilot acceptance
Find **two independent credible sources** for one building-related fact and one resident-related fact where possible. Use real, directly linked evidence, not generated claims. Keep the first four records intact and `REVIEW` unless a human approves a targeted change.

## Orchestrator integration
Collect assistants A-E outputs, deduplicate source candidates, compute coverage by **field family** and by **place category**, cluster new ideas, form a prioritized source-to-fields matrix and backlog. Output:
- `Field Atlas v1` (340 actual fields; no phantom fields);
- `Source Registry v1` (verified/candidate and license status);
- `Opportunity Atlas v1` (new fields & experiences, separate from current schema);
- `3 pilot proposals` with precise inputs, outputs, constraints and measurable value.

No live schema or publication changes without deliberate owner approval.
