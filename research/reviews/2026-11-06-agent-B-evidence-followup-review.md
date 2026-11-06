# Research B — focused evidence follow-up review (2026-11-06)

Source report: [2026-11-06-agent-B-evidence-followup.md](../reports/2026-11-06-agent-B-evidence-followup.md)
Status: **ADDITIONAL EVIDENCE / PARTIALLY FULFILLS FOLLOW-UP / NOT PRIMARY-SOURCE-VERIFIED**.

## Valuable new data
- For first time, all **four actual SPB MAP place IDs** addressed:
  - `SPB-PET-0001`: octagonal courtyard reportedly in income house N. S. Zanin, Maly Prospekt P.S. 1 lit. B (secondary: https://petersburg24.ru/place/dvor-vosmiugolnik).
  - `SPB-PET-0002`: Batman courtyard reportedly in income house R. A. Diderichs, Bolshoy Prospekt P.S. 104. Candidate ownership from 1913 directory indirectly transcribed at https://prawdom.ru/dom.php?hm=Bolshoj+P.S.+spb_104 ; original facsimile NOT read.
  - `SPB-PET-0003`: Benois complex, now distinguish Kamenoostrovsky 26/28 and historical Kronverkskaya 23/59 → later 29/37 **according to named research**; historical transition date unknown.
  - `SPB-PET-0011`: Lidval complex; 3 façade addresses cited; exact per-corpus identities still require geometry.
- Historical address books: RNB Vivaldi digital `bx000020053` for 1903 established, but **no original person row accessed**. Better lead: `Весь Петербург` 1913 section IV column 34, *secondary transcription* of Diderichs ownership.
- Archival **locators provided for Lidval** from Maria Rozanova's study: TsGIA SPb fond 515, opis 1, delo 7840; TsGA SPb fond 4304 opis 1, dela 942–955. These are referenced in a published study, not pages independently retrieved.
- **Benois archival study** by V.S. Izmozik & N.B. Lebina cites house books and archival files, with separate apartments for Kirov (no.20), Zinoviev (no.118), etc. Useful refutation: widely repeated claim that Kirov directly succeeded Zinoviev in the same apartment is reported as false; must not flatten both addresses.
- Ten candidate `person-place-relation` records with evidence grade B/C/D, **zero A**. These are a ready review queue, not approved resident facts.
- Real broadening: ordinary residents, housing costs, crowdedness, occupational geography, migration and household change, avoiding extrapolation from elite-only cases.

## Critical data corrections
1. **Report internally contradicts itself:** row 6 of 10-record table says `M. S. Chudov, from 1930, RESIDED_AT in apartment 40`; later §6 explicitly says Chudov **moved OUT** in 1930. Therefore **REJECT `start_date=1930`**; set timebound `before 1930; departure 1930 as reported, awaiting source audit`.
2. `owned_property_at` (Zanin, Diderichs) ≠ `resided_at`. Courtyards are not building residences; relationships should attach to containing building or historical holding after verification.
3. `Ida Lidval apartment 18 until 1915` does NOT establish residency throughout every year before 1915. `F. Lidval 1903–1918` secondary period and `apartment 23` scholarly account must not be treated as a single fully attested person+apartment+period record.
4. Source archive **locator or an author's citation** is a lead to primary evidence, not direct inspection of that evidence. Zero grade A facts, no automatic publishing.
5. Benois 23/59 → 29/37 is valuable historical-address hypothesis documented by research; independently check cross-era numbering, corpus and precise dates with an official archive/map.
6. Production `SPB-PET` IDs were associated by name and public source; the agent did not inspect the canonical Sheet's four address records. Need this join verified.
7. Source legal reuse and privacy remain unknown; no bulk scraping, image rehosting or publicizing private current residences.

## Prioritized single-page follow-up (not another broad report)
A. Retrieve/verify **one facsimile** of `Весь Петербург` 1913, section IV, column 34, and transcribe Diderichs `owner/address/year` with direct image locator. If viewer blocks access, state exact blocker and use a permitted manual editorial check.
B. Verify **one archive dossier** `TsGIA SPb f.515 op.1 d.7840` or `TsGA SPb f.4304 op.1 d.942` in the archival catalogue (catalog ID, title, date range, scan access); do not claim original folio read without doing so.
C. Resolve **Chudov 1930 departure** inconsistency and correct example row before reusing it.
D. Independently verify courtyard ↔ containing building relationship via at least 2 sources and distinguish same parcel vs building/courtyard section.
E. Provide a concise machine-readable `10 candidates` CSV with explicit separate date precision and `source_page`, `review_state`, `primary_seen`, `license_state`, rather than another essay.

## Orchestration decision
Archive candidate evidence. **No publication / no automatic import.** Give priority to a tiny rights-conscious evidence prototype, correcting Chudov's date before entering any value. Agent B second-stage status **received, partially fulfilled**.
