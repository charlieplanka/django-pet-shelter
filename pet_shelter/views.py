from pet_shelter.models import Pet
from django.views.generic import DetailView, TemplateView, ListView


class PetDetailView(DetailView):
    model = Pet


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class PetsListView(ListView):
    model = Pet

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # filter
        if get_params.get('filter'):
            qs = qs.filter(specie__title=get_params.get('filter'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_pets'] = Pet.objects.all()
        return context
