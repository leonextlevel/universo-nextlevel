import django_filters

from .models import Cenario


class CenarioFilter(django_filters.FilterSet):
    class Meta:
        model = Cenario
        fields = {
            'nome': ['icontains'],
        }
