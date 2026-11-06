# SPB MAP — Review of Agent D source-feasibility follow-up (2026-11-06)

[Full D follow-up](../reports/2026-11-06-agent-D-source-feasibility-followup.md).

**CLASSIFICATION: UNIQUE, MATERIAL NEW EVIDENCE / PARTIALLY VERIFIED FIVE SOURCE LEADS / THREE PILOTS SPECS (NOT EXECUTED).**

## Evidence contribution
|Source|Specific identifier/item|Readiness|Actual limitation|
|---|---|---|---|
|SPb data portal|Old housing technical-passport dataset `69`, possible endpoint `/api/v1/datasets/69/versions/latest/data/`|INVESTIGATE|Historical 2015 API only; no current dataset document, rows, schema, license or working endpoint validated in 2026.|
|OSM|New Holland relation `1576204`, indirectly retrieved from Wikidata P402|REVIEW|Actual OSM feature tags and geometry not fetched; no valid importing GIS layer until direct extraction and ODbL compliance assessed.|
|Wikidata|New Holland `Q2367357`, Q claims P31/P131/P625/P402/P5381|IMPORT candidate for CC0 identifiers with provenance|Individual assertions may lack references and the apparent heritage ID must match *the designated legal entity*, not entire historic site by assumption.|
|GBIF|Earthworm dataset `e52aacbf-c701-462b-b68f-346502fbc270`, DOI `10.15468/rcjcq6`|INVESTIGATE|Dataset-level only, **zero Petersburg occurrence gbifIDs**, date of scientific publication may be confused with observation date; published dataset-specific license needs preserving.|
|TsGA industrial archives|Krasny Treugolnik fund `Р-1360`, opis 1, cases 2/3/8/9/12; 1917 and 1918 headcount metadata|REVIEW for facts; LINK for documents|Original case leaves and digitized plan not read. Archive fund inventory references are meaningful provenance, not blanket rights to reproduce scans.|

Specific firm/building distinction: Wikidata `Q112033468` for enterprise vs `Q4239624` for complex (as supplied); don't merge. From fund notes historical address Obvodny Kanal 134–138, period-specific product and employment statistics. Years 1917/1918 snapshots are not comparable automatically.

## Important defects and scope correction
1. Agent D's **Pilot A is titled 'four existing SPB MAP records' but includes New Holland and Krasny Treugolnik**, neither of which belongs to our actual four. The actual IDs are:
   `SPB-PET-0001` Octagon, `SPB-PET-0002` Batman Diderichs at Bolshoy pr. P.S. 104, `SPB-PET-0003` Benois, `SPB-PET-0011` Lidval. Reject that claim of coverage. New Holland/Krasny are **NEW experimental entities** only, no invented place_ids.
2. OSM relation `1576204` is evidence of external identifier **not** evidence that the API was successfully read or that a reliable polygon has been matched.
3. GBIF metadata describes regional extent, **not eight validated Petersburg observations**. Need individual `gbifID`, coordinates, uncertainty, source and precise event/published date before an ecological map.
4. Tech/passport portal API described using a 2015 source, not current 2026 live working access. Keep INVESTIGATE.
5. Archive case 12 (site plan) is a catalogue entry, **not obtained georeferenced source image**. Do not infer historical parcel polygons from its title.
6. Scope includes past 26 opportunity ideas but second-stage proof only for a few sources. Avoid a claim of completing a 26-row normalized ranking matrix.

## Integrated three bounded pilots: coordinator recommendation
1. **Existing-map identity + media (4 places, up to 4 records)**. Candidate evidence from A and C: octagonal courtyard Zanin building, Batman **Diderichs Bolshoy P.S. 104** (not Ioffe Rubinshteina 40), Benois multi-building, Lidval complex. Distinct source claims, exact photo licenses and object-match states. C's precise octagon viewpoint unresolved. **No canonical edits**.
2. **People/address evidence micro-pilot (max 10 claims)**. B's ten sourced candidates; correct Chudov 1930 as departure. All original archive-book scans pending and no automatic public import.
3. **New independent industrial knowledge entity (max 8 claims)**. Triangulate `Enterprise` vs `IndustrialComplex`, R-1360 archives, dated events, address and source records. SPB MAP `place_id` not assigned because it is not among four pilots. This is the most grounded novel thematic pilot. GBIF future phase following individual sample discovery.

## Targeted D close-out request
No more broad research. Ask **one specific question**: return corrected Pilot A table with **only the four genuine SPB-PET IDs**, and relabel New Holland/Red Triangle as external experimental entities; separately attempt **one individual GBIF occurrence** with valid Petersburg geometry (or explicitly 'none found'). Optional: directly fetch OSM relation `1576204` API response, no invention. No production writes.

## Decision
Report archived, criteria recorded. Realistic implementation is a research-side candidate registry and isolated sample first, not a bulk import or modifications to the canonical Google Sheet, map GeoJSON or publication gates. Evidence and license checks remain separate, with any uncertainty preserved.
