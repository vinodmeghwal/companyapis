from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewset

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)


urlpatterns = [
    path('', include(router.urls))
]
