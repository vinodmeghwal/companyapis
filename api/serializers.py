from rest_framework import serializers
from api.models import CompanyModel


class Companyserializer(serializers.HyperlinkedModelSerializer):
                class Meta:
                    model=CompanyModel
                    fields="__all__"
