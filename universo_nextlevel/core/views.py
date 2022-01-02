from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)

from django_twitch_auth.views import TwitchLoginMixin

from universo_nextlevel.mixins import RequestUserMixin

from .forms import CenarioForm
from .models import Cenario


class HomeView(TemplateView):
    template_name = 'core/home.html'


class LoginView(TwitchLoginMixin, TemplateView):
    template_name = 'core/login.html'


class CenarioListView(LoginRequiredMixin, ListView):
    model = Cenario
    paginate_by = 6


class CenarioCreateView(LoginRequiredMixin, RequestUserMixin, CreateView):
    model = Cenario
    form_class = CenarioForm
    success_url = reverse_lazy('cenario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Cenário'
        return context


class CenarioUpdateView(LoginRequiredMixin, RequestUserMixin, UpdateView):
    model = Cenario
    form_class = CenarioForm
    success_url = reverse_lazy('cenario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Cenário'
        return context


class CenarioDetailView(LoginRequiredMixin, DetailView):
    model = Cenario
    context_object_name = 'cenario'


@login_required
def cenario_delete_view(request, pk):
    cenario = get_object_or_404(Cenario, pk=pk)
    cenario.delete()
    return redirect(reverse('cenario_list'))
