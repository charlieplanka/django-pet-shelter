from django.urls import path
from .views import pets, PetDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', pets, name='pets'),
    path('pets/<str:pk>', PetDetailView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)