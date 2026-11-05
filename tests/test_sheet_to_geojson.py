import io
import unittest
from tools.sheet_to_geojson import export

HEADERS=["place_id","Название","Категория","Широта","Долгота","Статус публикации","Почему интересно","Фото — статус лицензии","Основное фото — URL"]
BASE={"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[30.3,59.9]},"properties":{"id":"SPB-PET-0001","name":"Old","details":[{"text":"Preserved"}],"external_links":[{"url":"https://example.org"}]}}]}
def csvline(*cells):
    return ",".join(cells)+"\n"
def sample(*rows):
    return io.StringIO(csvline(*HEADERS)+"".join(csvline(*row) for row in rows))
GOOD=["SPB-PET-0001","Updated","Дворы","59.95","30.32","PUBLISHED_GITHUB","New","",""]

class PipelineTests(unittest.TestCase):
    def test_preserves_unmapped_fields(self):
        result=export(sample(GOOD),BASE)
        f=result["features"][0]
        self.assertEqual(f["properties"]["name"],"Updated")
        self.assertEqual(f["properties"]["details"],BASE["features"][0]["properties"]["details"])
        self.assertEqual(f["geometry"]["coordinates"],[30.32,59.95])
        self.assertEqual(export(sample(GOOD),BASE),result)
    def test_duplicate_rejected(self):
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            export(sample(GOOD,GOOD),BASE)
    def test_coordinate_validation(self):
        row=GOOD.copy();row[3]="0"
        with self.assertRaisesRegex(ValueError,"Coordinates"):
            export(sample(row),BASE)
    def test_unverified_photo_rejected(self):
        row=GOOD.copy();row[-1]="https://example.org/photo.jpg"
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

if __name__=="__main__": unittest.main()
