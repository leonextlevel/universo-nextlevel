from django import forms

from .models import Cenario


class CenarioForm(forms.ModelForm):

    class Meta:
        model = Cenario
        fields = [
            'nome',
            'imagem',
        ]

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if self.instance and not self.instance.pk:
            self.instance.criador = self.request_user
        return super().save(commit=commit)
