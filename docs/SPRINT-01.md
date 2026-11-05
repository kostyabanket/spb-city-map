# Sprint 01 — canonical Sheet → reviewed GeoJSON

Status: implementation in isolated branch; **not published**.

The sole editorial source is the tab `Единая база` in the linked canonical Google Sheet. Place key is `place_id`, not column number or row number. Existing GeoJSON is a publication baseline, not an editor.

## Workflow
1. Create a Google Cloud service account with **read-only** Sheets scope. Share the canonical sheet only with that account (Viewer). Do not make the Sheet public.
2. In GitHub repo Actions secrets add `GOOGLE_SERVICE_ACCOUNT_JSON` containing the service-account JSON. Never commit it.
3. After the workflow file is available on the default branch, manually start workflow `Sheet to GeoJSON preview`. It fetches the Sheet and validates a generated preview; **it never publishes**.
4. Review the logged diff. Only after explicit approval run the generator with `--output data/places.geojson`, review and commit the output.
5. Verify the live map and all four cards on mobile.

Local preview: `python tools/sheet_to_geojson.py --csv path/to/export.csv --check` (no write). To save an **unpublished preview**: `python tools/sheet_to_geojson.py --csv path/to/export.csv --output sheet-preview.geojson`. Only after reviewing the diff and explicitly approving release: `python tools/sheet_to_geojson.py --csv path/to/export.csv --output data/places.geojson --apply`. A semantically identical export never writes any file.

## Conservative publication policy
- Only previously existing place IDs and rows marked `PUBLISHED_GITHUB`, `PUBLISHED`, or `APPROVED`. **Rows with `Статус редакции` other than `APPROVED` / `VERIFIED` are left byte-for-byte equivalent at the feature level** (except output serialization). This is intentional: all four pilot rows are currently `REVIEW`.
- Preserve GeoJSON fields not mapped from the Sheet, notably editorial details, evidence arrays, existing historical-photo attribution and external links. A blank Sheet field never deletes a published value.
- Reject duplicate IDs, unexpected disappearance/addition, invalid or out-of-region coordinates, invalid photo links and insufficient photo attribution/license.
- Do not emit the 305 speculative fields, research notes, personal fields or Sheet contents. Row publication status is NOT verification of individual facts. Historic factual verification remains editorial work.
- Deliberately do not rewrite multi-value links/sources until a lossless structured contract is agreed.
- No automatic publishing; maintain previous Git commit as recovery.

## Follow-up
A separate PR can introduce one personal category filter with `localStorage`, checked in a browser and on a phone; no accounts or backend required.

## Verified source observations (2026-11-05)
All four canonical IDs match `data/places.geojson`. The Google Sheet displays geographic decimals with commas under Russian locale (e.g. `30,293621`); numeric parsing handles both dots and commas. All four editorial rows currently have `REVIEW` status, so the guarded preview must not replace their published text. A passing unit test does **not** mean Google service-account credentials are configured, a live Sheet pull succeeded, or mobile QA was completed.

## Live connector read-only cross-check (2026-11-05)
Read A1:AI5 from canonical Sheet through connected Google Drive and compared to `main:data/places.geojson`. Four IDs unique and matched; all names, geographic coordinates, and photo status flags matched. All four rows were `REVIEW` + `PUBLISHED_GITHUB`, therefore the approval gate intentionally produces a semantic no-op. This connector check is **not** proof that GitHub's service-account workflow has authenticated: setting up that credential remains outstanding.
