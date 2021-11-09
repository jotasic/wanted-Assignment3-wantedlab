from rest_framework      import status
from rest_framework.test import APITestCase


class CreateCompanyViewTest(APITestCase):
    maxDiff = None
    
    def test_create_success(self):
        data = """{
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH"
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15"
                    }
                }
            ]
        }"""

        response = self.client.post('/companies', data=data, content_type='application/json', HTTP_x_wanted_language='tw')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_data = {
        "company_name": "LINE FRESH",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
            ],
        }

        self.assertEqual(response.json(), expected_data)
        self.assertEqual(response.headers.get('x-wanted-language'), 'tw')


    def test_create_success_notag(self):
        data = """{
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH"
            },
            "tags": [
            ]
        }"""

        response = self.client.post('/companies', data=data, content_type='application/json', HTTP_x_wanted_language='tw')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_data = {
        "company_name": "LINE FRESH",
        "tags": [],
        }

        self.assertEqual(response.json(), expected_data)
        self.assertEqual(response.headers.get('x-wanted-language'), 'tw')

    def test_create_failed_duto_tag_not_exsist(self):
        data = """{
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH"
            },

        }"""

        response = self.client.post('/companies', data=data, content_type='application/json', HTTP_x_wanted_language='tw')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_failed_duto_comany_name_not_exsist(self):
        data = """{
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15"
                    }
                }
            ]
        }"""

        response = self.client.post('/companies', data=data, content_type='application/json', HTTP_x_wanted_language='tw')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)