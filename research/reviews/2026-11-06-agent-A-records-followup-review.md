# SPB MAP — Agent A record-level follow-up review (2026-11-06)

**Status: UNIQUE SECOND-STAGE EVIDENCE REPORT; mixed quality; CRITICAL cross-place false match detected.**

## Ground truth: actual published SPB MAP records
Directly read `data/places.geojson` (2026-11-06):
- `SPB-PET-0001` courtyard octagon: Малый проспект Петроградской стороны, 1Б; coords [30.293621,59.954845].
- `SPB-PET-0002` Batman courtyard: **Большой проспект Петроградской стороны, 104**; coords [30.313014,59.967286]; described as in R. A. Diderichs house.
- `SPB-PET-0003` Benois complex: Каменноостровский пр., 26–28.
- `SPB-PET-0011` Lidval complex: Каменноостровский пр., 1–3.

## Critical error / prohibit wrong join
Agent A's eight-row table **row 4** assigns `SPB-PET-0002` to **Rubinshteina 40/11** and candidate FIAS `e10dcf32-23c4-45e1-a3a3-0006a9e72836`. This is a **different courtyard** at the House of Shneer-Zalman Ioffe, corner of Zagorodny prospekt 11 / Rubinshteina 40. It is also called a cat/Batman shaped courtyard, causing an ambiguous *name alias*. Do **not** merge with our Diderichs `SPB-PET-0002` (Bolshoy pr. P.S. 104).

Independent public evidence:
- https://commons.wikimedia.org/wiki/File:%D0%94%D0%B2%D0%BE%D1%80-%D0%BA%D0%BE%D0%BB%D0%BE%D0%B4%D0%B5%D1%86_%22%D0%91%D1%8D%D1%82%D0%BC%D0%B5%D0%BD%22.jpg describes Diderichs at Bolshoy P.S. 104.
- https://prawdom.ru/dom.php?hm=Bolshoj+P.S.+spb_104 describes House of Diderichs.
- https://www.narubinsteina.ru/cultur/istoriya-domov/doxodnyij-dom-shneera-zalmana-ioffa-rubinshtejna-40/11.html says oval courtyard at Rubinshteina 40 resembles cat/Batman.
- https://visit-petersburg.ru/leisure/places/dokhodnyy-dom-korfa-ioffa/ describes Ioffe site at Zagorodny 11 / Rubinshteina 40.

**Disposition:** row 4 `REJECT_FOR_PLACE_ID` (not necessarily a false external address GUID; it may be valid for a different place). Keep as an optional separate discovered POI candidate, NOT linked to `SPB-PET-0002`. Retain actual Diderichs building identity with `needs_primary_geometry_review`.

## Findings by original report rows
1. `0001` Domscanner `0f881fcc-e9f0-4d03-a29b-a8375709bf71`: address GUID **secondary listed**, unverified against primary FIAS XML. Candidate for historical Zanin **building**, not independent courtyard; note 1б лит. А vs colloquial 1Б.
2. `0001` Zanin heritage examination at https://www.saintcapybaras.com/Home/GetStateExamination/10732?page=94; archive mentions octagonal interior courtyard: strong link from **examination**; precise full text / photo page should be inspected before accepting subpart polygon. Address lit. A is official building designation; street `1Б` alone isn't explicit `liter B`.
3. `0001` Wikivoyage monument catalogue `7831482000` derived catalogue ID; **not verified as national EGROKN registered designation number**.
4. `0002` Rubinshteina 40/11 `e10dcf32-...`: **WRONG PLACE**. Suppress from mapping to existing SPB-PET-0002; no primary FIAS validation.
5. `0003` openaddress `d8aefd4f-ff00-463e-8401-79483a41d44e`: source-specific ID; FIAS type not confirmed. Cadastral number `78:07:0003074:2029` secondary. Only candidate for building liter A, not whole Benois complex.
6. `0003` derived EGROKN `781610410690006`: candidate heritage designation from Wikivoyage; separately verify exact designated object vs whole complex.
7. `0003` catalogue `7832874000`: candidate courtyard building liter V; heritage coverage not independently verified.
8. `0011` historical legal list no. `54, 54.1` — *list positions*, NOT formal EGROKN numbers; distinction between Lidval complex and protected facades meaningful.
9. **OSM** 0 direct way/relation IDs; provider search links are not item records. No geometry has been successfully matched; no imported polygons.

## Useful independently corroborated date split
Official Petrograd administration https://www.gov.spb.ru/gov/terr/reg_petrograd/news/172412/ confirms Benois Kamenoostrovsky street-facing phase 1911–1912 and Kronverkskaya phase 1913–1914. Separate later/earlier court building is a further claim that must be attached to its own heritage/physical building identity.

## Follow-up ask to Agent A — sharply narrowed
1. **Correct entity matching first.** Explicitly state `SPB-PET-0002 = Bolshoy prospekt P.S., 104 = Diderichs` and `Rubinshteina 40/11 = Ioffe` is another site. Withdraw row 4. No edits to production.
2. Find one actual unique **OSM way/relation link** for Diderichs or Zanin with coordinates/geometry and explain polygon vs nearby points; if unavailable report unresolved, not guessed. If API fails, use a permitted public OSM GUI item URL manually.
3. Verify one primary FIAS record via FNS XML or official service, clearly naming `OBJECTGUID/OBJECTID` and layer: address vs building.
4. Verify one official heritage register **item** by matching *legal designation identity* (not derived Wikivoyage category ID) to a physical building or ensemble.
5. End with a corrected **maximum 8-row evidence register** with `place_id`, `source_record_id`, `entity_type`, `match_decision`, `source_directness`, `license_state`, `needs_review`. Do not do another architecture overview.

## Publication/engineering gate
No updates to Google Sheet, canonical records, production map or automatically published building facts. The user should send ONE correction message to A now; C and D follow-up reports still awaited.
