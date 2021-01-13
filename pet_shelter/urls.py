from django.urls import path
from .views import pets
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', pets, name='pets')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)