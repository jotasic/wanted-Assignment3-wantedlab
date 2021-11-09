from django.shortcuts import render, get_object_or_404
from django.http      import JsonResponse

from rest_framework import status
from rest_framework.response   import Response
from rest_framework.views  import APIView

from rest_framework.serializers import Serializer

from companies.models               import Company, Tag
from companies.serializers.detail_serializers import CompanySerializer

class DetailView(APIView):
    def get(self, request, name):
        language = request.headers.get("x-wanted-language", "ko")

        c = {f'company_name__{language}' : name}

        company = get_object_or_404(Company, **c)
        company_serializer = CompanySerializer(company, many=False)

        tag_list = [] 
        print(company_serializer.data)
        for tag in company_serializer.data['tags']:
            tag_list.append(tag["tag_name"][language])

        results = {
                "company_name" : company_serializer.data["company_name"][language],
                "tags" : tag_list
        }
        return Response(results, status=status.HTTP_200_OK)