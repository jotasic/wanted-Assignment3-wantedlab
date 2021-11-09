from rest_framework import response, views, status

from companies.serializers.list_serializers   import CompanySerializer, TagSerializer
from companies.models                         import Company, Tag

from django.core.exceptions                   import ObjectDoesNotExist

class CompanySearchAPIView(views.APIView):

    def get(self, request):
        search  = request.GET.get('query', None)
        results = []

        if search is None:
            return response.Response(results, status=status.HTTP_200_OK)

        language = request.headers.get('x-wanted-language', 'ko')

        c = {f'company_name__{language}__icontains': search}

        companies = Company.objects.filter(**c)
        company_serializer = CompanySerializer(companies, many=True)

        results = [{
             "company_name" : company['company_name'][language]
        } for company in company_serializer.data]

        return response.Response(results, status=status.HTTP_200_OK)