from django.urls         import path

from .views.detail_views import DetailView
from .views.create_views import CompanyCreateAPIView


urlpatterns = [
    path('companies/<str:name>', DetailView.as_view(), name ='companyname'),
    path('companies', CompanyCreateAPIView.as_view()),
]