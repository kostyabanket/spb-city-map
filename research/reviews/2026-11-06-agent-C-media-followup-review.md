# SPB MAP — Research C imagery follow-up QA (2026-11-06)

**Classification: NEW SUPPLEMENT, not duplicate.** [Preserved 11-asset report and checks](../reports/2026-11-06-agent-C-verified-media-followup.md).

## Item-level verification
- **READY FOR EDITORIAL IMAGE PILOT (licensing/source metadata supported; not imported):**
  - `0002` [Batman courtyard, Diderichs, Bolshoy P.S. 104](https://commons.wikimedia.org/wiki/File:Двор-колодец_%22Бэтмен%22.jpg). Commons directly lists author Бегущий из города; 2020-09-18; camera 59.967286,30.313014; CC BY-SA 4.0. This independently confirms our current identity against agent A's incorrect Rubinshteina 40/11 claim.
  - `0003` [BenoisHouse.jpg](https://commons.wikimedia.org/wiki/File:BenoisHouse.jpg) Potekhin; 2008-12-30; CC BY-SA 3.0.
  - `0011` [LidvalHouse.jpg](https://commons.wikimedia.org/wiki/File:LidvalHouse.jpg) Potekhin; January 2010; CC BY-SA 3.0.
- **NEEDS EXACT VIEWPOINT CHECK:** `0001` [Malyy PS 1B 01.jpg](https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg) Ekaterina Borisova; 2017-05-25; CC BY-SA 4.0; Commons identifies Zanin building but not necessarily the octagonal courtyard opening.
- **NEEDS RIGHTS JURISDICTION REVIEW:** [Benois House SPb 1916.jpg](https://commons.wikimedia.org/wiki/File:Benois_House_SPb_1916.jpg), public domain marked on Commons, but mark isn't a grant/license and underlying scan/original-work provenance must be checked.
- Other Commons files claimed in the report need individual verification before usage (2024 Benois courtyard, 2025 Lidval details, 2022 repainting).
- **PASTVU** [244685](https://pastvu.com/p/244685), [1428318](https://pastvu.com/p/1428318), [2662942](https://pastvu.com/p/2662942) reported by agent C. Rights NOT established: LINK ONLY. The claimed live API sample was not independently reproduced by coordinator; distinguish researcher-reported API output from coordinator-verifiable response.

## Critical model design
Represent asset links as `VisualAsset` connected to `DepictedPlace` and `CameraPose`, with `LicenseRecord` and `PublicationDecision`. Copyright permission vs evidence that photo depicts *the particular sub-place* are **independent gates**. For a courtyard, photo of the main building facade does not automatically qualify as photo of the octagonal area.

## Follow-up restricted to 0001
Agent C needs at most one **true photo of the octagonal part of courtyard 0001**, with source card, license, actual view evidence (or mark 'not confirmed'). Also if possible, give one complete machine-readable asset record (file page, creator, CC URL, source media URL, date, depicted place, attribution line and any transformations).

## Proposed first deployment-free test
Assemble four `candidate_media` records (one per real place), not published:
- `0002` Batman CC BY-SA 4.0 confirmed.
- `0003` Benois modern CC BY-SA 3.0 confirmed.
- `0011` Lidval modern CC BY-SA 3.0 confirmed.
- `0001` Zanin photo **pending viewpoint validation**, no confirmed octagon view.
Gates: legal permission, object matching, attribution with source/author/license/changes, no prohibited copy. Test legacy photo field export via E review, without changing canonical sheet.

## Decision
Keep C report and media catalogue. No further broad survey requested. Last-mile task is choosing a confirmed 0001 courtyard view + preparing 4 compatible asset metadata records; don't mass-download or populate Sheet automatically.
