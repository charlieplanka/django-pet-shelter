from django.urls import path
from .views import PetDetailView, PetsListView, ContactsView, add_pet
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import login, logout

urlpatterns = [
    path('', PetsListView.as_view(), name='pets'),
    path('pets/<str:pk>', PetDetailView.as_view()),
    path('pets/new/', add_pet, name='add_pet'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
