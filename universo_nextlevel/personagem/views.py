from django.views.generic import ListView

from universo_nextlevel.personagem.models import Personagem


class PersonagemListView(ListView):
    model = Personagem
