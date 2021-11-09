import jsonschema

from rest_framework   import serializers

from companies.models import Company, Tag


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id', 'company', )
        model   = Tag
        
    def to_representation(self, instance):
        language = self.context['request']._request.headers.get('x-wanted-language', 'ko')
        data = super().to_representation(instance)
        
        return data['tag_name'].get(language, None)

    def validate_tag_name(self, value):
        tag_name_schema = {
            'title'             : 'company_name',
            'version'           : 1,
            'type'              : 'object',
            'patternProperties' : {
                '.*': { 'type': 'string' },
            }
        }
        
        try:
            jsonschema.validate(schema=tag_name_schema, instance=value)
        except jsonschema.ValidationError as e:
            raise serializers.ValidationError(f' {e.instance} is not of type \"{e.validator_value}\"')
        return value


class CompanyCreateSerializer(serializers.ModelSerializer):
    tags = TagCreateSerializer(source='tag_set', many=True)

    class Meta:
        fields = ('company_name', 'tags', )
        model   = Company

    def create(self, validated_data):
        new_company = Company.objects.create(company_name=validated_data.pop('company_name'))

        for tag in validated_data.pop('tag_set'):
            Tag.objects.create(company=new_company, **tag)

        return new_company
    
    def to_representation(self, instance):
        language = self.context['request']._request.headers.get('x-wanted-language', 'ko')
        data = super().to_representation(instance)

        data['company_name'] = data['company_name'].get(language, None)
        data['tags'] = [tag for tag in data['tags'] if tag is not None]

        return data

    def validate_company_name(self, value):
        company_name_schema = {
            'title'             : 'company_name',
            'version'           : 1,
            'type'              : 'object',
            'patternProperties' : {
                '.*': { 'tpye': 'string' },
            },
        }

        try:
            jsonschema.validate(schema=company_name_schema, instance=value)
        except jsonschema.ValidationError as e:
            raise serializers.ValidationError(f' {e.instance} is not of type \"{e.validator_value}\"')
        return value