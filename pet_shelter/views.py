from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Pet, Specie
from .forms import PetForm


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
        context['species'] = Specie.objects.all()
        return context


def add_pet(request):
    data = {}
    if request.user.is_authenticated:
        data['username'] = request.user.username
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.photo = request.FILES['photo']
            pet.save()
        return redirect('/')
    else:
        data['form'] = PetForm()
        return render(request, 'add_pet.html', data)
