from django.urls                  import path

from companies.views.create_views import CompanyCreateCreateAPIView

urlpatterns = [
    path('', CompanyCreateCreateAPIView.as_view()),
]