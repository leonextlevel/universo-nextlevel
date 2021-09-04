from django import forms

from .models import Personagem


class PersonagemForm(forms.ModelForm):

    class Meta:
        model = Personagem
        fields = [
            'nome',
            'idade',
            'sexo',
            'profissao',
            'caracteristica_marcante',
            'background',
            'tendencia',
            'descricao_fisica',
            'imagem_perfil',
        ]
