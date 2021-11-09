from rest_framework      import status
from rest_framework.test import APITestCase

from companies.models    import Company

class CompanySearchViewTest(APITestCase):
    maxDiff = None

    def setUp(self):
        Company.objects.create(
            id = 1,
            company_name = {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH"
            }
        )
        Company.objects.create(
            id = 2,
            company_name = {
                "ko" : "원티드랩",
                "en" : "wantedlab",
                "ja" : "ワンティードラップ"
            }
        )
    
    def tearDown(self):
        Company.objects.all().delete()

    #회사명 자동완성
    def test_company_name_autocomplete(self):
        header = {"HTTP_x-wanted-language": "ko"}
        response = self.client.get(
                '/search?query=라인', content_type='application/json', **header
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {"company_name" : "라인 프레쉬"}
            ]

        self.assertEqual(response.json(), expected_data)

    #한국어로 검색하는데 결과가 나오는 경우    
    def test_search_in_korean_with_result(self):
        header = {"HTTP_x-wanted-language": "ko"}
        response = self.client.get(
            '/search?query=라인', content_type='application/json', **header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [{
        "company_name" : "라인 프레쉬",
        }]

        self.assertEqual(response.json(), expected_data)

    #영어로 검색하는데 결과가 없는 경우
    def test_search_in_english_no_result(self):
        header = {"HTTP_x-wanted-language": "en"}

        response = self.client.get(
            '/search?query=naver', content_type='application/json', **header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = []
        self.assertEqual(response.json(), expected_data)