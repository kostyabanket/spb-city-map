"""Research-only tests; never write to the canonical Sheet or public GeoJSON."""
import json
import unittest
from research.pipeline.address_to_card_dryrun import build_card, normalize_address, ROOT


class AddressToCardDryRunTests(unittest.TestCase):
    def test_four_locked_pilot_places_are_projected(self):
        for pid in ("SPB-PET-0001", "SPB-PET-0002",
                    "SPB-PET-0003", "SPB-PET-0011"):
            with self.subTest(place_id=pid):
                card = build_card(place_id=pid)
                self.assertEqual(card["place_id"], pid)
                self.assertFalse(card["ready_for_publication"])
                self.assertFalse(card["published_data_modified"])
                self.assertTrue(card["rubrics"])
                self.assertNotEqual(card["district_geometry_check"], "VERIFIED")

    def test_address_variant_matches_locked_diderichs_place(self):
        card = build_card(address="Большой пр. П. С., 104")
        self.assertEqual(card["place_id"], "SPB-PET-0002")

    def test_does_not_match_similar_named_wrong_courtyard(self):
        with self.assertRaisesRegex(ValueError, "not match|Unknown|False"):
            build_card(place_id="SPB-PET-0002",
                       address="улица Рубинштейна, 40/11")

    def test_does_not_publish_new_place_from_address_only(self):
        with self.assertRaisesRegex(ValueError, "Unknown or ambiguous"):
            build_card(address="Большой проспект Петроградской стороны, 999")

    def test_0001_has_licensed_commons_photo_candidate(self):
        card = build_card(place_id="SPB-PET-0001")
        media = next(x for x in card["rubrics"] if x["rubric_id"] == "modern_media")
        self.assertEqual(media["items"][0]["license"], "CC BY-SA 4.0")
        self.assertTrue(media["items"][0]["file_page"].startswith("https://commons.wikimedia.org/"))

    def test_0003_preserves_multiple_people_without_fictional_dates(self):
        card = build_card(place_id="SPB-PET-0003")
        people = next(x for x in card["rubrics"] if x["rubric_id"] == "people")["items"]
        self.assertGreaterEqual(len(people), 3)
        chudov = next(x for x in people if "Чудов" in x["person_name"])
        self.assertIsNone(chudov["valid_from"])
        self.assertEqual(chudov["valid_to"], "1930")
        self.assertEqual(chudov["date_precision"], "DEPARTURE_YEAR_ONLY")

    def test_only_nonempty_sections_are_projected(self):
        card = build_card(place_id="SPB-PET-0002")
        shown = {r["rubric_id"] for r in card["rubrics"]}
        self.assertNotIn("legends", shown)
        self.assertNotIn("culture", shown)
        self.assertTrue(set(card["empty_rubrics_hidden"]).isdisjoint(shown))

    def test_dry_run_is_deterministic(self):
        a = build_card(place_id="SPB-PET-0002")
        b = build_card(place_id="SPB-PET-0002")
        self.assertEqual(json.dumps(a, sort_keys=True),
                         json.dumps(b, sort_keys=True))

    def test_normalization_is_not_fuzzy_name_matching(self):
        self.assertEqual(normalize_address("Большой пр. П. С., 104"),
                         normalize_address("Большой проспект Петроградской стороны, 104"))
        self.assertNotEqual(normalize_address("Большой пр. П. С., 104"),
                            normalize_address("Рубинштейна, 40/11"))


if __name__ == "__main__":
    unittest.main()
