"""Check proposed 340->rubric map and 15 provider decisions remain coherent."""
import csv
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class ResearchSchemaContractTests(unittest.TestCase):
    def test_all_340_legacy_positions_preserved_exactly(self):
        original=ROOT/"research/field-inventory-340.csv"
        mapping=ROOT/"research/schema/RUBRIC-MAP-340-2026-11-06.csv"
        with original.open(encoding="utf-8",newline="") as f:
            old=list(csv.DictReader(f))
        with mapping.open(encoding="utf-8",newline="") as f:
            new=list(csv.DictReader(f))
        self.assertEqual(len(old),340)
        self.assertEqual(len(new),340)
        for o,n in zip(old,new):
            self.assertEqual(n["position"],o["position"])
            self.assertEqual(n["original_field_header"],o["field_header"])
            self.assertEqual(n["catalog_group"],o["group"])
            self.assertTrue(n["rubric_id"])
        self.assertTrue(all(x["semantic_status"]=="LEGACY_COMPAT_PRESERVE" for x in new[:35]))

    def test_manifest_is_bounded_to_four_petrogradsky_ids(self):
        path=ROOT/"research/pipeline/SOURCE-REGISTRY-PETROGRADSKY-V1.json"
        source=json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(source["source_count"],15)
        self.assertEqual(len(source["sources"]),15)
        self.assertEqual(len({x["id"] for x in source["sources"]}),15)
        self.assertEqual(len(source["scope"]["allowed_existing_ids"]),4)
        self.assertEqual(source["scope"]["new_public_place_ids"],"DISABLED")
        self.assertIs(source["scope"]["auto_import_to_site"],False)
        self.assertTrue(all(s["automation"] for s in source["sources"]))
        hold=[x for x in source["sources"] if x["priority"]=="HOLD"]
        self.assertEqual(len(hold),2)
        self.assertTrue(all(x["automation"]=="DO_NOT_SCHEDULE" for x in hold))


if __name__=="__main__":
    unittest.main()
