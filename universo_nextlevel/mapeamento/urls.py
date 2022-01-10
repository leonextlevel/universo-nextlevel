from django.urls import path, include

from .views import MapeamentoSelect, NacaoListView


urlpatterns = [
    path('select/', MapeamentoSelect.as_view(), name='mapeamento_select'),
    path('nacao/', include([
        path('list/', NacaoListView.as_view(), name='nacao_list'),
    ])),
]
