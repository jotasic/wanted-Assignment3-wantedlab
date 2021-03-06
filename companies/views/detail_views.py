from django.http.response      import Http404
from rest_framework            import status
from rest_framework.response   import Response
from rest_framework.views      import APIView

from companies.models                         import Company
from companies.serializers.detail_serializers import CompanySerializer


class DetailView(APIView):
    def get(self, request, name):
        language = request.headers.get("x-wanted-language", "ko")
        
        found_company = None
        companies = Company.objects.filter(company_name__icontains=name)
        for company in companies:
            if name in company.company_name.values():
                found_company = company
                break

        if not found_company:
            raise Http404()

        company_serializer = CompanySerializer(found_company, many=False)

        tag_list = []
        for tag in company_serializer.data['tags']:
            if tag["tag_name"].get(language) is not None:
                tag_list.append(tag["tag_name"][language])

        results = {
                "company_name" : company_serializer.data["company_name"][language],
                "tags"         : tag_list
        }
        return Response(results, status=status.HTTP_200_OK)