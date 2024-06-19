# companyapi/urls.py

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # other URL patterns if any
    path('api/v1/', include('api.urls')),  # Use 'api.urls' if 'api' has its own URLs defined
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
