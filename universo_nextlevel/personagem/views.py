from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    TemplateView,
)

from .models import Personagem
from .forms import PersonagemForm


class HomeView(TemplateView):
    template_name = 'home.html'


class PersonagemListView(ListView):
    model = Personagem


class PersonagemCreateView(CreateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')


class PersonagemUpdateView(UpdateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')
