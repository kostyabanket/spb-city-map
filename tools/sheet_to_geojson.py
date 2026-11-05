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
        if (row.get("Основное фото — URL") or "").strip():
            if photo_status != "LICENSE_VERIFIED": raise ValueError(pid+": photo lacks verified license")
            for header,key in PHOTO.items():
                value=(row.get(header) or "").strip()
                if value: props[key]=value
            for key in ("photo_url","photo_source_url"):
                if not url_ok(props.get(key,"")): raise ValueError(pid+": bad "+key)
            if not props.get("photo_author") or not props.get("photo_license"):
                raise ValueError(pid+": incomplete photo attribution")
        historic=(row.get("Историческое фото — URL") or "").strip()
        if historic:
            for header,key in HISTORIC.items():
                value=(row.get(header) or "").strip()
                if value: props[key]=value
            if not url_ok(historic) or not props.get("historic_photo_license"):
                raise ValueError(pid+": historical photo has missing license or invalid URL")
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
    p.add_argument("--output",default="data/places.geojson",type=Path)
    p.add_argument("--check",action="store_true",help="Compare with baseline without writing")
    args=p.parse_args()
    with args.csv.open(encoding="utf-8-sig",newline="") as stream:
        output=export(stream,json.loads(args.existing.read_text(encoding="utf-8")))
    content=json.dumps(output,ensure_ascii=False,indent=2)+"\n"
    if args.check:
        import difflib
        old=args.existing.read_text(encoding="utf-8")
        print("".join(difflib.unified_diff(old.splitlines(True),content.splitlines(True),fromfile=str(args.existing),tofile="sheet-preview.geojson"))[:30000])
        print("Validated",len(output["features"]),"places; no files written")
    else:
        args.output.write_text(content,encoding="utf-8")
        print("Wrote",args.output)

if __name__=="__main__":main()
