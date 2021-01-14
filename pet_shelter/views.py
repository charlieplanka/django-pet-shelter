from pet_shelter.models import Pet
from django.template import loader
from django.http import HttpResponse


def pets(request):
    template = loader.get_template('pets.html')
    pets = Pet.objects.order_by('-arrival_date').all()
    pets_data = {'pets': pets}
    return HttpResponse(template.render(pets_data, request))