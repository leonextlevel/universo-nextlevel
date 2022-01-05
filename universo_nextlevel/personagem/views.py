from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
)
from django_filters.views import FilterView

from universo_nextlevel.mixins import RequestUserMixin
from .models import Personagem
from .forms import PersonagemForm
from .filtersets import PersonagemFilter


class PersonagemListView(LoginRequiredMixin, FilterView):
    model = Personagem
    paginate_by = 6
    template_name = 'personagem/personagem_list.html'
    filterset_class = PersonagemFilter


class PersonagemCreateView(LoginRequiredMixin, RequestUserMixin, CreateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Personagem'
        return context


class PersonagemUpdateView(LoginRequiredMixin, RequestUserMixin, UpdateView):
    model = Personagem
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Personagem'
        return context


class PersonagemDetailView(LoginRequiredMixin, DetailView):
    model = Personagem
    context_object_name = 'personagem'


@login_required
def personagem_delete_view(request, pk):
    personagem = get_object_or_404(Personagem, pk=pk)
    personagem.delete()
    return redirect(reverse('personagem_list'))
