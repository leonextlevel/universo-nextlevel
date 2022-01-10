from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
)

from .models import Nacao


class MapeamentoSelect(LoginRequiredMixin, TemplateView):
    template_name = 'mapeamento/mapeamento_select.html'


class NacaoListView(LoginRequiredMixin, ListView):
    model = Nacao
