from pet_shelter.models import Pet
from django.views.generic import DetailView, TemplateView, ListView


class PetDetailView(DetailView):
    model = Pet


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class PetsListView(ListView):
    model = Pet
