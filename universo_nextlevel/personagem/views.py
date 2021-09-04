from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    TemplateView,
    DetailView,
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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Personagem'
        return context


class PersonagemUpdateView(UpdateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Personagem'
        return context


class PersonagemDetailView(DetailView):
    model = Personagem
    context_object_name = 'personagem'
