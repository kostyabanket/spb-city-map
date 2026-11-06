# Proposed patch: keep photo_status synchronized on approved image import
**Status: OFFLINE-TESTED PROPOSAL; NOT APPLIED TO PRODUCTION**

Target (future, only after approval): `tools/sheet_to_geojson.py`.

```diff
@@
         if (row.get("Основное фото — URL") or "").strip():
             if photo_status != "LICENSE_VERIFIED": raise ValueError(pid+": photo lacks verified license")
             for header,key in PHOTO.items():
                 value=(row.get(header) or "").strip()
                 if value: props[key]=value
+            props["photo_status"] = photo_status
             for key in ("photo_url","photo_source_url"):
                 if not url_ok(props.get(key,"")): raise ValueError(pid+": bad "+key)
```

## Isolated execution
Applied to a local copy of the exporter, never to GitHub production code.

|Test fixture|Exit|Expected|
|---|---|---|
|Four `REVIEW` records|`0`|No semantic changes; no files written|
|`APPROVED`, photo without licensed status|`1`|Rejected|
|`APPROVED`, license and attribution supplied|`0`|Reviewable diff; no files written|
|`APPROVED`, missing author|`1`|Rejected|
|`APPROVED`, HTTP source URL|`1`|Rejected|
|Duplicate `place_id`|`1`|Rejected|

Additional direct Python assertion on the output object: `photo_status == LICENSE_VERIFIED` and `photo_license == CC BY-SA 4.0` for the isolated `SPB-PET-0001` fixture.

**Scope limitation:** these execution tests use representative four-row fixtures. Separate read-only Google Sheets and GitHub connector comparisons used the actual live 35×4 cells and full current GeoJSON; the full unmodified production baseline has not been used as a byte-exact local file in the executable Python test.

**Still needed:** (1) populated and verified `photo_license_url` in the published record or a controlled license registry; (2) a separate historically sourced image rights gate; (3) an exact 35×4 + full GeoJSON executable test before a production change; (4) editorial approval for the `SPB-PET-0001` image. None of this patch is active.

[Full publication gate and findings](./QA-PHOTO-PUBLICATION-GATE-2026-11-06.md).
