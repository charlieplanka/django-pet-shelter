from pet_shelter.models import Pet
from django.template import loader
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView


class PetDetailView(DetailView):
    model = Pet


class ContactsView(TemplateView):
    template_name = 'contacts.html'


def pets(request):
    template = loader.get_template('pets.html')
    pets = Pet.objects.order_by('-arrival_date').all()
    pets_data = {'pets': pets}
    return HttpResponse(template.render(pets_data, request))


