from rest_framework import response, views, status

from companies.serializers.list_serializers   import CompanySerializer, TagSerializer
from companies.models                         import Company, Tag

from django.core.exceptions                   import ObjectDoesNotExist

class CompanySearchAPIView(views.APIView):

    def get(self, request):
        try:    
            search = request.GET.get('query', None)
            if request.headers['x-wanted-language'] is False:
                language = 'ko'
            else :
                language = request.headers['x-wanted-language']

            c = {f'company_name__{language}__icontains': search}

            companies = Company.objects.filter(**c)
            company_serializer = CompanySerializer(companies, many=True)

            results = [{
                "company_name" : company['company_name'][language]
            } for company in company_serializer.data]

            return response.Response(results, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return response.Response(results, status=status.HTTP_404_NOT_FOUND)