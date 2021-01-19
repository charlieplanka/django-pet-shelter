from django.urls import path
from .views import pets, PetDetailView, ContactsView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', pets, name='pets'),
    path('pets/<str:pk>', PetDetailView.as_view()),
    path('contacts', ContactsView.as_view(), name='contacts')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)