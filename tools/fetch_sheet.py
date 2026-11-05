#!/usr/bin/env python3
"""Fetch canonical Sheet securely with Google service account into a local CSV, no public sharing."""
import argparse
import csv
import io
import os
from pathlib import Path
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SHEET_ID="1cnVo0uyw6BxY0rPlkKHv0buSx8MTRatYZR1tHzloC88"
SHEET_RANGE="'Единая база'!A1:MB200"
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,default=Path("/tmp/spb-map-sheet.csv"))
    args=p.parse_args()
    raw=os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not raw: raise SystemExit("GOOGLE_SERVICE_ACCOUNT_JSON is required; do not publish credentials")
    import json
    credentials=service_account.Credentials.from_service_account_info(
        json.loads(raw),scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    credentials.refresh(Request())
    url=f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{requests.utils.quote(SHEET_RANGE,safe='')} "
    response=requests.get(url.strip(),headers={"Authorization":"Bearer "+credentials.token},timeout=30)
    response.raise_for_status()
    values=response.json().get("values",[])
    if not values: raise SystemExit("No spreadsheet data")
    with args.output.open("w",encoding="utf-8",newline="") as f:
        writer=csv.writer(f);writer.writerows(values)
    print("Fetched",len(values)-1,"rows securely")

if __name__=="__main__":main()
