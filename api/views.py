from django.shortcuts import render
from rest_framework import viewsets
from api.models import CompanyModel
from api.serializers import  Companyserializer
# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=CompanyModel.objects.all()
    serializer_class= Companyserializer