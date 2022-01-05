import django_filters

from .models import Personagem


class PersonagemFilter(django_filters.FilterSet):
    class Meta:
        model = Personagem
        fields = {
            'nome': ['icontains'],
            'sexo': ['exact'],
            'profissao': ['icontains'],
            'tendencia': ['exact'],
            'idade': ['gte', 'lte'],
        }
