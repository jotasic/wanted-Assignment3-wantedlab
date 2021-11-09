from rest_framework   import serializers

from companies.models import Company, Tag




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tag
        fields = ['tag_name']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = ['company_name']