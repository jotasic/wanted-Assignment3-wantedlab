from django.urls         import path

from .views.detail_views import DetailView
from .views.create_views import CompanyCreateAPIView
from .views.list_views   import CompanySearchAPIView


urlpatterns = [
    path('companies/<str:name>', DetailView.as_view(), name ='companyname'),
    path('companies', CompanyCreateAPIView.as_view()),
    path('companies/search', CompanySearchAPIView.as_view())
]