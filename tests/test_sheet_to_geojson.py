import io
import unittest
from tools.sheet_to_geojson import export

HEADERS=["place_id","Название","Категория","Широта","Долгота","Статус публикации","Почему интересно","Фото — статус лицензии","Основное фото — URL","Статус редакции"]
BASE={"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[30.3,59.9]},"properties":{"id":"SPB-PET-0001","name":"Old","details":[{"text":"Preserved"}],"external_links":[{"url":"https://example.org"}]}}]}
def csvline(*cells):
    return ",".join(cells)+"\n"
def sample(*rows):
    return io.StringIO(csvline(*HEADERS)+"".join(csvline(*row) for row in rows))
GOOD=["SPB-PET-0001","Updated","Дворы","59.95","30.32","PUBLISHED_GITHUB","New","","","APPROVED"]

class PipelineTests(unittest.TestCase):
    def test_preserves_unmapped_fields(self):
        result=export(sample(GOOD),BASE)
        f=result["features"][0]
        self.assertEqual(f["properties"]["name"],"Updated")
        self.assertEqual(f["properties"]["details"],BASE["features"][0]["properties"]["details"])
        self.assertEqual(f["geometry"]["coordinates"],[30.32,59.95])
        self.assertEqual(export(sample(GOOD),BASE),result)
    def test_unapproved_editorial_text_never_overwrites_publication(self):
        row=GOOD.copy();row[-1]="REVIEW"
        result=export(sample(row),BASE)
        self.assertEqual(result["features"][0]["properties"]["name"],"Old")
        self.assertEqual(result["features"][0]["geometry"]["coordinates"],[30.3,59.9])
    def test_review_rows_produce_semantically_identical_feature(self):
        row=GOOD.copy()
        row[HEADERS.index("Статус редакции")]="REVIEW"
        actual=export(sample(row),BASE)
        self.assertEqual(actual,BASE)

    def test_comma_decimal_coordinates(self):
        row=GOOD.copy()
        row[HEADERS.index("Широта")]="59,95"
        row[HEADERS.index("Долгота")]="30,32"
        values=io.StringIO()
        import csv
        writer=csv.writer(values)
        writer.writerow(HEADERS)
        writer.writerow(row)
        values.seek(0)
        actual=export(values,BASE)
        self.assertEqual(actual["features"][0]["geometry"]["coordinates"],[30.32,59.95])

    def test_duplicate_rejected(self):
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            export(sample(GOOD,GOOD),BASE)
    def test_coordinate_validation(self):
        row=GOOD.copy();row[3]="0"
        with self.assertRaisesRegex(ValueError,"Coordinates"):
            export(sample(row),BASE)
    def test_unverified_photo_rejected(self):
        row=GOOD.copy();row[HEADERS.index("Основное фото — URL")]="https://example.org/photo.jpg"
        with self.assertRaisesRegex(ValueError,"photo lacks verified"):
            export(sample(row),BASE)
    def test_unapproved_row_cannot_remove_existing_place(self):
        row=GOOD.copy();row[5]="DRAFT"
        with self.assertRaisesRegex(ValueError,"Publication set differs"):
            export(sample(row),BASE)
    def test_unreviewed_new_place_rejected(self):
        row=GOOD.copy();row[0]="SPB-PET-9999"
        with self.assertRaisesRegex(ValueError,"Unreviewed new place"):
            export(sample(row),BASE)


    def _media_sample(self, row, author="Екатерина Борисова",
                      license_name="CC BY-SA 4.0",
                      source="https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg"):
        # Use the same test header contract plus the additional photo columns.
        import csv
        fields = HEADERS + ["Фото — автор", "Фото — лицензия", "Фото — источник"]
        values = row.copy()
        values[HEADERS.index("Основное фото — URL")] = (
            "https://commons.wikimedia.org/wiki/Special:FilePath/Малый_ПС_1Б_01.jpg"
        )
        values[HEADERS.index("Фото — статус лицензии")] = "LICENSE_VERIFIED"
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(fields)
        writer.writerow(values + [author, license_name, source])
        output.seek(0)
        return output

    def test_approved_cc_photo_updates_status_and_license_url(self):
        import copy
        baseline = copy.deepcopy(BASE)
        baseline["features"][0]["properties"]["photo_status"] = "NO_VERIFIED_LICENSED_PHOTO"
        result = export(self._media_sample(GOOD), baseline)
        props = result["features"][0]["properties"]
        self.assertEqual(props["photo_status"], "LICENSE_VERIFIED")
        self.assertEqual(props["photo_author"], "Екатерина Борисова")
        self.assertEqual(props["photo_license"], "CC BY-SA 4.0")
        self.assertEqual(props["photo_license_url"],
                         "https://creativecommons.org/licenses/by-sa/4.0/")
        self.assertEqual(props["details"], baseline["features"][0]["properties"]["details"])

    def test_review_does_not_update_photo_status_or_photo(self):
        import copy
        baseline = copy.deepcopy(BASE)
        baseline["features"][0]["properties"]["photo_status"] = "NO_VERIFIED_LICENSED_PHOTO"
        row = GOOD.copy()
        row[HEADERS.index("Статус редакции")] = "REVIEW"
        self.assertEqual(export(self._media_sample(row), baseline), baseline)

    def test_missing_photo_author_rejected(self):
        with self.assertRaisesRegex(ValueError, "incomplete photo attribution"):
            export(self._media_sample(GOOD, author=""), BASE)

    def test_invalid_photo_source_url_rejected(self):
        with self.assertRaisesRegex(ValueError, "bad photo_source_url"):
            export(self._media_sample(GOOD, source="http://example.org/photo.jpg"), BASE)

    def test_photo_license_status_is_required(self):
        import csv
        content = self._media_sample(GOOD)
        values = list(csv.reader(content))
        values[1][HEADERS.index("Фото — статус лицензии")] = "NO_VERIFIED_LICENSED_PHOTO"
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerows(values)
        output.seek(0)
        with self.assertRaisesRegex(ValueError, "photo lacks verified license"):
            export(output, BASE)

    def test_cc_by_sa_3_license_link(self):
        result = export(self._media_sample(GOOD, license_name="CC BY-SA 3.0"), BASE)
        self.assertEqual(result["features"][0]["properties"]["photo_license_url"],
                         "https://creativecommons.org/licenses/by-sa/3.0/")

if __name__=="__main__": unittest.main()
