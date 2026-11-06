# SPB MAP — End-to-end export gate / proposed first photo change
**2026-11-06 · RESEARCH ONLY · NO PRODUCTION WRITES**

## Sources actually inspected
- Canonical Google Sheet, tab «Единая база», `A1:AI5` (35 columns, 4 rows), accessed in read-only mode.
- GitHub `data/places.geojson`, **4 full baseline features** (the file itself was not edited).
- GitHub `tools/sheet_to_geojson.py`, existing Python exporter source.
- C's Commons photo evidence: https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg , attributed to **Екатерина Борисова**, 2017-05-25, **CC BY-SA 4.0**.

## Test levels — distinguish carefully

|Test|What actually ran|Result|
|---|---|---|
|Source repo/Python exporter on small fixture|Original exporter logic copied to local isolated Python script, CLI `--check` executed for 6 scenarios|**PASS**: REVIEW unchanged, missing photo rights rejected, properly licensed APPROVED shows diff without writing, missing author/bad HTTP/duplicate ID rejected|
|Actual full live 35-column header + 4-row data versus baseline full GeoJSON|Google Sheets connector + GitHub connector fetched true live data; in-memory cross-check verified all 35 headings, all 4 IDs, coords and source code branches|**PASS**: 4/4 identity and coordinates, 35/35 headers, all rows `REVIEW`, no source file writes|
|Actual full baseline + actual 35×4 spreadsheet data, original Python CLI `--check`|**Not executed in same container**: connector fetched records cannot be transferred to the sandbox as a full byte-exact snapshot with current tooling|**NOT TESTED** as literal end-to-end CLI. Do not claim a full executable round-trip|
|APPROVED scenario on **real metadata** from `0001` and full GeoJSON feature|Direct source-to-target mapping evaluated **in memory** under verified exporter code|**FAIL / publication blocker**: photo is added but `photo_status` remains `NO_VERIFIED_LICENSED_PHOTO`|

## Critical mismatch: exporter does not update photo status

The real exporter has a mapping `PHOTO` for:
- `Основное фото — URL → photo_url`
- `Фото — автор → photo_author`
- `Фото — лицензия → photo_license`
- `Фото — источник → photo_source_url`

When a sheet row becomes `APPROVED`, the script validates `Фото — статус лицензии == LICENSE_VERIFIED`, then populates those four properties. **It does not set `props.photo_status`.**

For the actual `SPB-PET-0001` baseline:
- Before: `photo_url=""`, `photo_status="NO_VERIFIED_LICENSED_PHOTO"`.
- After a hypothetical APPROVED import: `photo_url` becomes the Commons image, **but `photo_status` still falsely says** `NO_VERIFIED_LICENSED_PHOTO`.
- `photo_license_url` also is not populated by exporter, even though other 3 public pilot features store a CC license hyperlink. The canonical 35 columns contain photo license name but **no dedicated license URL** field, so a controlled mapping or license lookup is needed before public integration.

## Secondary issue: historical media
The importer for `Историческое фото — URL` only checks that URL is HTTPS and `historic_photo_license` text is nonempty. That is **not proof** the original work is public domain or otherwise licensed for publication. `0003` live Sheet currently lists a historic image with `Public domain (согласно странице файла)`. This must remain gated by an explicit editorial rights decision; do not automatically infer that nonempty text means verified permission.

## Minimal proposed changes (NOT APPLIED)
1. Add an explicitly guarded assignment in the importer when non-empty primary photo is accepted:
   `props["photo_status"] = photo_status`.
2. Map a known allowed CC BY-SA license string to a verified license URI for Commons (`CC BY-SA 4.0 → https://creativecommons.org/licenses/by-sa/4.0/`; `CC BY-SA 3.0 → https://creativecommons.org/licenses/by-sa/3.0/`) or maintain a structured validated rights record. **Do not infer permissions from arbitrary non-CC text.**
3. Enforce per-item historic-photo license review; distinguish `license_description` from `rights_review_status`; never auto-publish historical picture when only a public-domain claim exists.
4. Add explicit automated tests for: `REVIEW` never changes public feature, `APPROVED` + verified Commons photo updates all photo metadata atomically, missing attribution or invalid HTTPS rejected, old `photo_status` cannot be retained after successful image import, historic-photo rights require review.

## Candidate edit for future editorial approval: `SPB-PET-0001`
- Place: **Двор-восьмиугольник**, same coordinates and address; do not change feature ID or point.
- New source: https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg .
- Suggested display URL (NOT used in production): `https://commons.wikimedia.org/wiki/Special:FilePath/%D0%9C%D0%B0%D0%BB%D1%8B%D0%B9_%D0%9F%D0%A1_1%D0%91_01.jpg?width=960`.
- Photographer: Екатерина Борисова; date 2017-05-25; CC BY-SA 4.0; license URL https://creativecommons.org/licenses/by-sa/4.0/ .
- Viewpoint: evidence/reviewer C regards as actual eight-sided courtyard sky opening; exact camera location UNKNOWN.
- **Desired changes only after editorial approval and exporter fix**: `photo_url`, `photo_author`, `photo_license`, `photo_license_url`, `photo_source_url`, `photo_status`. Preserve review rules, attributed Commons source, license and changed-image notice.

## Recommendation and decision point
**NO-GO for applying public photo today through the existing importer** until the stale `photo_status` issue is fixed and release tests pass. This is a small engineering issue, not a reason to reopen broad A–E research.

**NEXT**: prepare a narrow exporter fix and Python tests in a nonproduction branch/isolated copy; validate on exact repo baseline; request explicit user/editorial permission before any changes to live code, Google Sheet, or public GeoJSON.
