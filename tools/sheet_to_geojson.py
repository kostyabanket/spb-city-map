#!/usr/bin/env python3
"""SPB MAP: guarded, deterministic CSV -> GeoJSON preview. No network or writes to Sheets."""
import argparse
import csv
import json
import math
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = ("place_id", "Название", "Категория", "Широта", "Долгота", "Статус публикации")
MAPPING = {
    "Название": "name", "Категория": "category", "Адрес": "address",
    "Почему интересно": "why", "Краткая история": "description",
    "Что заметить": "look", "Условия доступа": "access_note",
    "Точность координат": "location_precision",
}
PHOTO = {
    "Основное фото — URL": "photo_url", "Фото — автор": "photo_author",
    "Фото — лицензия": "photo_license", "Фото — источник": "photo_source_url",
}
HISTORIC = {
    "Историческое фото — URL": "historic_photo_url",
    "Историческое фото — подпись": "historic_photo_caption",
    "Историческое фото — лицензия": "historic_photo_license",
}
ALLOWED = {"PUBLISHED_GITHUB", "APPROVED", "PUBLISHED"}
SHEET_ID = "1cnVo0uyw6BxY0rPlkKHv0buSx8MTRatYZR1tHzloC88"

def url_ok(value):
    p = urlparse(value)
    return p.scheme == "https" and bool(p.netloc) and not p.username and not p.password

def parse_coords(row):
    try:
        lat, lon = float(row["Широта"].replace(",", ".")), float(row["Долгота"].replace(",", "."))
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid coordinates") from exc
    if not all(math.isfinite(v) for v in (lat,lon)) or not (59 <= lat <= 61 and 29 <= lon <= 32):
        raise ValueError("Coordinates outside Saint Petersburg sanity bounds")
    return [lon,lat]

def export(csv_file, existing):
    rows = list(csv.DictReader(csv_file))
    if not rows: raise ValueError("No sheet rows")
    missing = set(REQUIRED) - set(rows[0])
    if missing: raise ValueError("Missing headers: " + ", ".join(sorted(missing)))
    if existing.get("type") != "FeatureCollection": raise ValueError("Invalid baseline GeoJSON")
    baseline = {f["properties"]["id"]: f for f in existing["features"]}
    if len(baseline) != len(existing["features"]): raise ValueError("Duplicate baseline place IDs")
    updated,seen = [],set()
    for row in rows:
        pid = (row.get("place_id") or "").strip()
        if not pid: continue
        if pid in seen: raise ValueError("Duplicate place_id: "+pid)
        seen.add(pid)
        if row["Статус публикации"].strip().upper() not in ALLOWED: continue
        if pid not in baseline: raise ValueError("Unreviewed new place: "+pid)
        f = json.loads(json.dumps(baseline[pid],ensure_ascii=False))
        coords = parse_coords(row)
        editorial_status = (row.get("Статус редакции") or "").strip().upper()
        if editorial_status not in {"APPROVED", "VERIFIED"}:
            # Existing public information remains as-is until the editorial row is approved.
            updated.append(f)
            continue
        f["geometry"]["coordinates"] = coords
        props = f["properties"]
        for header,key in MAPPING.items():
            value = (row.get(header) or "").strip()
            if value: props[key] = value
        photo_status = (row.get("Фото — статус лицензии") or "").strip()
        photo_values = {key: (row.get(header) or "").strip()
                        for header, key in PHOTO.items()}
        if photo_values["photo_url"]:
            if photo_status != "LICENSE_VERIFIED":
                raise ValueError(pid + ": photo lacks verified license")
            # Use fields from the new row, not the previous photograph's author.
            if any(not photo_values[key] for key in
                   ("photo_author", "photo_license", "photo_source_url")):
                raise ValueError(pid + ": incomplete photo attribution")
            cc_license_urls = {
                "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/",
                "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
            }
            license_url = cc_license_urls.get(photo_values["photo_license"])
            if not license_url:
                raise ValueError(pid + ": unsupported photo license; rights review required")
            for key in ("photo_url", "photo_source_url"):
                if not url_ok(photo_values[key]):
                    raise ValueError(pid + ": bad " + key)
            props.update(photo_values)
            props["photo_status"] = photo_status
            props["photo_license_url"] = license_url
        historic = (row.get("Историческое фото — URL") or "").strip()
        if historic:
            if historic != baseline[pid]["properties"].get("historic_photo_url", ""):
                raise ValueError(pid + ": new historical photo requires separate rights review")
            # Existing historical image metadata stays unchanged; a mere
            # public-domain label is not authorization for a new image.
        props["id"]=pid
        updated.append(f)
    if set(baseline) != {f["properties"]["id"] for f in updated}:
        raise ValueError("Publication set differs from baseline; manual review required before adding/removing places")
    updated.sort(key=lambda f:f["properties"]["id"])
    return {"type":"FeatureCollection","features":updated}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--csv",required=True, type=Path,help="CSV export from canonical single tab")
    p.add_argument("--existing",default="data/places.geojson",type=Path)
    p.add_argument("--output",default="sheet-preview.geojson",type=Path)
    p.add_argument("--check",action="store_true",help="Compare with baseline without writing")
    p.add_argument("--apply",action="store_true",help="Explicitly authorize replacing the current published GeoJSON")
    args=p.parse_args()
    if args.check and args.apply:
        p.error("--check and --apply cannot be combined")
    if args.output.resolve() == args.existing.resolve() and not (args.check or args.apply):
        p.error("Refusing to overwrite published GeoJSON without --apply")
    if args.apply and args.output.resolve() != args.existing.resolve():
        p.error("--apply must target --existing")
    baseline_text=args.existing.read_text(encoding="utf-8")
    with args.csv.open(encoding="utf-8-sig",newline="") as stream:
        baseline=json.loads(baseline_text)
        output=export(stream,baseline)
    if output == baseline:
        print("Validated",len(output["features"]),"places; no semantic changes, no files written")
        return
    content=json.dumps(output,ensure_ascii=False,indent=2)+"\n"
    if args.check:
        import difflib
        print("".join(difflib.unified_diff(baseline_text.splitlines(True),content.splitlines(True),fromfile=str(args.existing),tofile=str(args.output)))[:30000])
        print("Validated",len(output["features"]),"places; no files written")
    else:
        args.output.write_text(content,encoding="utf-8")
        print("Wrote",args.output)

if __name__=="__main__":main()
