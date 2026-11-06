#!/usr/bin/env python3
"""Read-only SPB MAP P0 adapter: project data -> proposed rubric card.

This is NOT a web crawler and DOES NOT verify external archival evidence.
It can only project existing four Petrogradsky pilot identities, known
Commons candidate metadata and the ten P2 research claims into an offline
draft.  A real source-collection runner must implement provider adapters.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALLOWED = frozenset(("SPB-PET-0001", "SPB-PET-0002",
                     "SPB-PET-0003", "SPB-PET-0011"))
RUBRIC_NAMES = {
    "chronology": "История по годам",
    "architecture": "Архитектура и авторы",
    "details": "Двор и детали",
    "people": "Люди и адреса",
    "events": "События и эпохи",
    "uses": "Что было здесь",
    "modern_media": "Фото сегодня",
    "historical_media": "Фото раньше",
    "legends": "Легенды и версии",
    "culture": "Кино, книги, искусство",
    "access": "Как увидеть и попасть",
    "nearby": "Рядом и маршруты",
    "sources": "Источники и проверка",
}


def normalize_address(value: str) -> str:
    """Minimal explicit variants; never use fuzzy name-only joining."""
    s = value.casefold().replace("ё", "е").strip()
    s = re.sub(r"\bпр\.(?=\s|$)", "проспект", s)
    s = re.sub(r"\bп\s*\.\s*с\s*\.", "петроградской стороны", s)
    s = re.sub(r"[.,;]", " ", s)
    return " ".join(s.split())


def read_inputs(root: Path):
    geo = json.loads((root / "data/places.geojson").read_text(encoding="utf-8"))
    places = geo["features"]
    with (root / "research/pilots/p1-four-places-media-candidates.csv").open(
            encoding="utf-8", newline="") as f:
        photos = {row["place_id"]: row for row in csv.DictReader(f)}
    people_doc = json.loads((root / "data/pilot-history.json").read_text(encoding="utf-8"))
    return places, photos, people_doc["records"]


def claim(value, source_id="SPB_MAP_CURRENT_GEOJSON"):
    return {"value": value, "source_id": source_id,
            "review_status": "PROJECT_CONTENT_NOT_PRIMARY_VERIFIED"}


def build_card(place_id=None, address=None, root=ROOT):
    places, photos, people = read_inputs(Path(root))
    matching = [f for f in places if f["properties"]["id"] == place_id] if place_id else []
    if not matching and address:
        a = normalize_address(address)
        matching = [f for f in places
                    if normalize_address(f["properties"].get("address", "")) == a]
    if len(matching) != 1:
        raise ValueError("Unknown or ambiguous exact pilot object: do not create a public place_id")
    place = matching[0]
    props = place["properties"]
    pid = props["id"]
    if pid not in ALLOWED:
        raise ValueError("Outside the four pre-established Petrogradsky pilot IDs")
    if place_id and address and normalize_address(props["address"]) != normalize_address(address):
        raise ValueError("The address does not match the locked existing place_id")
    if pid == "SPB-PET-0002" and "рубиншт" in (address or "").casefold():
        raise ValueError("False Batman courtyard join: Rubinshteina != Diderichs")

    p = photos.get(pid) or {}
    related = [x for x in people if x.get("place_id") == pid]
    rubrics = []
    def add(key, records):
        if records:
            rubrics.append({"rubric_id": key, "title": RUBRIC_NAMES[key], "items": records})

    if props.get("description"):
        add("chronology", [claim(props["description"])])
    if props.get("look"):
        add("details", [claim(props["look"])])
    if related:
        add("people", [{
            "person_name": x["person_name"],
            "relation_type": x["relation_type"],
            "historical_address": x["historical_address"],
            "apartment": x.get("apartment") or None,
            "valid_from": x.get("valid_from") or None,
            "valid_to": x.get("valid_to") or None,
            "date_precision": x.get("date_precision"),
            "source_url": x.get("source_url"),
            "review_status": x.get("review_status"),
            "note": x.get("reliability_note"),
        } for x in related])
    if p.get("commons_file_url"):
        add("modern_media", [{
            "file_page": p["commons_file_url"],
            "author": p.get("photographer"),
            "photo_date": p.get("photo_date"),
            "license": p.get("license"),
            "license_url": p.get("license_url"),
            "viewpoint_status": p.get("viewpoint_status"),
            "review_status": p.get("editorial_status"),
            "rights_status": p.get("rights_status"),
        }])
    if props.get("access_note"):
        add("access", [claim(props["access_note"])])
    links = []
    for source in props.get("sources", []):
        if source.get("url"):
            links.append({"url": source["url"], "label": source.get("title") or "Источник"})
    for source in props.get("external_links", []):
        if source.get("url"):
            links.append({"url": source["url"], "label": source.get("label") or "Ссылка"})
    if links:
        add("sources", links)

    return {
        "status": "RESEARCH_DRAFT_NO_EXTERNAL_FETCH",
        "scope": "Петроградский район — existing four pilot records only",
        "district_geometry_check": "NOT_PERFORMED_EXISTING_ID_ONLY",
        "place_id": pid,
        "name": props["name"],
        "address": props["address"],
        "coordinates": place["geometry"]["coordinates"],
        "lead": props.get("why", ""),
        "rubrics": rubrics,
        "empty_rubrics_hidden": [k for k in RUBRIC_NAMES
                                if not any(r["rubric_id"] == k for r in rubrics)],
        "source_status": "PROJECT_AND_PILOT_RESEARCH_ONLY",
        "published_data_modified": False,
        "ready_for_publication": False,
        "notes": [
            "No web crawl or official district polygon verification performed.",
            "Media licenses and historic-address claims need per-item review.",
            "No generated place IDs, OSM geometry, official GAR numbers, or archival verification.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--place-id")
    parser.add_argument("--address")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--dry-run", action="store_true", required=True)
    args = parser.parse_args()
    if not args.place_id and not args.address:
        parser.error("provide --place-id or --address")
    try:
        result = build_card(args.place_id, args.address, args.root)
    except (ValueError, FileNotFoundError, KeyError, json.JSONDecodeError) as err:
        parser.exit(2, f"REVIEW_REQUIRED: {err}\n")
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
