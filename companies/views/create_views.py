from rest_framework.generics import CreateAPIView

from companies.serializers.create_serializers import CompanyCreateSerializer
from companies.models                         import Company


class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanyCreateSerializer
    
    def get_queryset(self):
        language        = self.request.headers.get('x-wanted-language', 'ko')
        language_filter = {f'company_name__{language}__isnull' : False}

        return Company.objects.prefetch_related('tag_set').filter(**language_filter)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyCreateSerializer

    @property
    def default_response_headers(self):
        header = super().default_response_headers
        
        try:
            header['x-wanted-language'] = self.request.headers.get('x-wanted-language', 'ko')
            return header

        except (TypeError, KeyError):
            return header