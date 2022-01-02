from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Atributo, Descricao, Personagem


class DescricaoForm(forms.ModelForm):

    class Meta:
        model = Descricao
        fields = [
            'altura',
            'cor_olho',
            'cor_cabelo',
            'cor_pele',
            'peso',
            'outras_caracteristicas',
        ]


class PersonagemForm(forms.ModelForm):
    # Campos para descrição
    altura = forms.IntegerField(min_value=0, max_value=220, required=False)
    cor_olho = forms.CharField(max_length=100, label="Cor do Olho", required=False)
    cor_cabelo = forms.CharField(max_length=100, label="Cor do Cabelo", required=False)
    cor_pele = forms.CharField(max_length=100, label="Cor da Pele", required=False)
    peso = forms.IntegerField(min_value=1, max_value=200, required=False)
    outras_caracteristicas = forms.CharField(widget=forms.Textarea, required=False)

    # Campos para atributos
    max_hp = forms.IntegerField(min_value=0, max_value=1000, required=False)
    max_mp = forms.IntegerField(min_value=0, max_value=1000, required=False)
    forca = forms.IntegerField(min_value=0, max_value=15, required=False)
    destreza = forms.IntegerField(min_value=0, max_value=15, required=False)
    precisao = forms.IntegerField(min_value=0, max_value=15, required=False)
    inteligencia = forms.IntegerField(min_value=0, max_value=15, required=False)
    sabedoria = forms.IntegerField(min_value=0, max_value=15, required=False)
    carisma = forms.IntegerField(min_value=0, max_value=15, required=False)
    resistencia = forms.IntegerField(min_value=0, max_value=15, required=False)
    foco = forms.IntegerField(min_value=0, max_value=15, required=False)
    esquiva = forms.IntegerField(min_value=0, max_value=15, required=False)
    sorte = forms.IntegerField(min_value=0, max_value=15, required=False)

    class Meta:
        model = Personagem
        fields = [
            'nome',
            'idade',
            'sexo',
            'profissao',
            'tendencia',
            'descricao',
            'atributo',
            'background',
            'caracteristica_marcante',
            'imagem',
            'cenario',
        ]

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super().__init__(*args, **kwargs)
        self.fields['cenario'].queryset = self.fields['cenario'].queryset.filter(criador=self.request_user)
        if self.instance and self.instance.descricao:
            self.fields['altura'].initial = self.instance.descricao.altura
            self.fields['cor_olho'].initial = self.instance.descricao.cor_olho
            self.fields['cor_cabelo'].initial = self.instance.descricao.cor_cabelo
            self.fields['cor_pele'].initial = self.instance.descricao.cor_pele
            self.fields['peso'].initial = self.instance.descricao.peso
            self.fields['outras_caracteristicas'].initial = self.instance.descricao.outras_caracteristicas
        if self.instance and self.instance.atributo:
            self.fields['max_hp'].initial = self.instance.atributo.max_hp
            self.fields['max_mp'].initial = self.instance.atributo.max_mp
            self.fields['forca'].initial = self.instance.atributo.forca
            self.fields['destreza'].initial = self.instance.atributo.destreza
            self.fields['precisao'].initial = self.instance.atributo.precisao
            self.fields['inteligencia'].initial = self.instance.atributo.inteligencia
            self.fields['sabedoria'].initial = self.instance.atributo.sabedoria
            self.fields['carisma'].initial = self.instance.atributo.carisma
            self.fields['resistencia'].initial = self.instance.atributo.resistencia
            self.fields['foco'].initial = self.instance.atributo.foco
            self.fields['esquiva'].initial = self.instance.atributo.esquiva
            self.fields['sorte'].initial = self.instance.atributo.sorte
            
    def clean(self):
        cleaned_data = super().clean()
        # Se algum dos campos de descrição vier com valor e outros não, levantar
        # exceção.
        self.descricao_dict = {
            'altura': cleaned_data['altura'],
            'cor_olho': cleaned_data['cor_olho'],
            'cor_cabelo': cleaned_data['cor_cabelo'],
            'cor_pele': cleaned_data['cor_pele'],
            'peso': cleaned_data['peso'],
            'outras_caracteristicas': cleaned_data['outras_caracteristicas'],
        }
        self.atributo_dict = {
            'max_hp': cleaned_data['max_hp'],
            'max_mp': cleaned_data['max_mp'],
            'forca': cleaned_data['forca'],
            'destreza': cleaned_data['destreza'],
            'precisao': cleaned_data['precisao'],
            'inteligencia': cleaned_data['inteligencia'],
            'sabedoria': cleaned_data['sabedoria'],
            'carisma': cleaned_data['carisma'],
            'resistencia': cleaned_data['resistencia'],
            'foco': cleaned_data['foco'],
            'esquiva': cleaned_data['esquiva'],
            'sorte': cleaned_data['sorte'],
        }
        if any(self.descricao_dict.values()) and not all(self.descricao_dict.values()):
            for key, value in self.descricao_dict.items():
                if not value:
                    self.add_error(key, "Campo requerido!")
        if any(self.atributo_dict.values()) and not all(self.atributo_dict.values()):
            for key, value in self.atributo_dict.items():
                if not value:
                    self.add_error(key, "Campo requerido!")

        return cleaned_data

    def save(self, commit: bool = True):
        if self.instance and not self.instance.pk:
            if commit and all(self.descricao_dict.values()):
                with transaction.atomic():
                    self.instance.descricao = Descricao.objects.create(**self.descricao_dict)
                    self.instance.atributo = Atributo.objects.create(**self.atributo_dict)
        elif self.instance and self.instance.pk:
            descricao = self.instance.descricao
            atributo = self.instance.atributo
            with transaction.atomic():
                if descricao is not None:
                    for key, value in self.descricao_dict.items():
                        setattr(descricao, key, value)
                    descricao.save()
                elif all(self.descricao_dict.values()):
                    self.instance.descricao = Descricao.objects.create(**self.descricao_dict)
                if atributo is not None:
                    for key, value in self.atributo_dict.items():
                        setattr(atributo, key, value)
                    atributo.save()
                elif all(self.descricao_dict.values()):
                    self.instance.atributo = Atributo.objects.create(**self.atributo_dict)
        return super().save(commit=commit)
