from rest_framework      import status
from rest_framework.test import APITestCase

from companies.models    import Company, Tag


class DetailViewTest(APITestCase):
    maxDiff = None

    def setUp(self):
        Company.objects.create(
            id = 1,
            company_name = {
                "ko" : "한국어회사1",
                "en" : "영어회사1",
                "ja" : "일본어회사1"
            }
        )
        Company.objects.create(
            id = 2,
            company_name = {
                "ko" : "한국어회사2",
                "en" : "영어회사2",
                "ja" : "일본어회사2"
            }
        )
        Tag.objects.create(
            id = 1,
            company_id = 1,
            tag_name = {
                "ko" : "한국어태그1-1",
                "en" : "영어태그1-1",
                "ja" : "일본어회사1-1"
            }
        )
        Tag.objects.create(
            id = 2,
            company_id = 1,
            tag_name = {
                "ko" : "한국어태그1-2",
                "en" : "영어태그1-2",
                "ja" : "일본어회사1-2"
            }
        )
        Tag.objects.create(
            id = 3,
            company_id = 1,
            tag_name = {
                "ko" : "한국어태그1-3",
                "en" : "영어태그1-3",
                "ja" : "일본어회사1-3"
            }
        )
        Tag.objects.create(
            id = 4,
            company_id = 2,
            tag_name = {
                "ko" : "한국어태그2-1",
                "en" : "영어태그2-1",
                "ja" : "일본어회사2-1"
            }
        )
        Tag.objects.create(
            id = 5,
            company_id = 2,
            tag_name = {
                "ko" : "한국어태그2-2",
                "en" : "영어태그2-2",
                "ja" : "일본어회사2-2"
            }
        )
        Tag.objects.create(
            id = 6,
            company_id = 2,
            tag_name = {
                "ko" : "한국어태그2-3",
                "en" : "영어태그2-3",
                "ja" : "일본어회사2-3"
            }
        )

    def tearDown(self):
        Company.objects.all().delete()
        Tag.objects.all().delete()

    def test_detail_view_success(self):
        header = {"HTTP_x-wanted-language": "en"}

        response = self.client.get(
            '/companies/한국어회사1', **header, content_type="application/json"
            )

        expected_data = {
            "company_name": "영어회사1",
            "tags": [
                "영어태그1-1",
                "영어태그1-2",
                "영어태그1-3"
            ]
        }
        self.assertEqual(response.json(), expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail_view_fail(self):
        header = {"x-wanted-language": "ko"}

        response = self.client.get(
            '/companies/없는회사', **header, content_type="application/json"
            )

        self.assertEqual(response.json(), {"detail" : "Not found."})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)