from django.db import models


class Company(models.Model):
    company_name = models.JSONField(default=dict)

    class Meta:
        db_table = 'companies'


class Tag(models.Model):
    company  = models.ForeignKey(Company, on_delete=models.CASCADE)
    tag_name = models.JSONField(default=dict)

    class Meta:
        db_table = 'tags'