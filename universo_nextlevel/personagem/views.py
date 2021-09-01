from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Personagem
from .forms import PersonagemForm


class PersonagemListView(ListView):
    model = Personagem


class PersonagemCreateView(CreateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')
