from django.db import models
from django.db.models.deletion import PROTECT

from universo_nextlevel.core.models import Cenario

from .choices import SexoChoices, TendenciaChoices


class Descricao(models.Model):
    altura = models.PositiveSmallIntegerField("Altura")
    cor_olho = models.CharField("Cor do olho", max_length=100)
    cor_cabelo = models.CharField("Cor do cabelo", max_length=100)
    cor_pele = models.CharField("Cor do pele", max_length=100)
    peso = models.PositiveSmallIntegerField("Peso")
    outras_caracteristicas = models.TextField("Outras Características")


class Atributo(models.Model):
    # Atributos Básicos
    max_hp = models.PositiveSmallIntegerField("HP Máximo")
    max_mp = models.PositiveSmallIntegerField("MP Máximo")

    # Atributos Principais
    forca = models.SmallIntegerField("Força")
    destreza = models.SmallIntegerField("Destreza")
    precisao = models.SmallIntegerField("Precisão")
    inteligencia = models.SmallIntegerField("Inteligência")
    sabedoria = models.SmallIntegerField("Sabedoria")
    carisma = models.SmallIntegerField("Carisma")
    resistencia = models.SmallIntegerField("Resistência")
    foco = models.SmallIntegerField("Foco")
    esquiva = models.SmallIntegerField("Esquiva")

    # Atributo Épico
    sorte = models.SmallIntegerField("Sorte")


class Personagem(models.Model):

    cenario = models.ForeignKey(Cenario, on_delete=models.CASCADE, verbose_name="Cenário")

    # Básico
    nome = models.CharField("Nome", max_length=100)
    idade = models.PositiveSmallIntegerField("Idade")
    sexo = models.CharField("Sexo", max_length=1, choices=SexoChoices.choices)
    profissao = models.CharField("Profissão", max_length=50)
    tendencia = models.CharField(
        "Tendência",
        max_length=2,
        choices=TendenciaChoices.choices,
    )

    descricao = models.OneToOneField(
        Descricao,
        on_delete=PROTECT,
        null=True,
        blank=True
    )

    atributo = models.OneToOneField(
        Atributo,
        on_delete=PROTECT,
        null=True,
        blank=True,
    )

    # Aprofudamento
    background = models.TextField("Background")
    caracteristica_marcante = models.TextField("Característica Marcante")

    imagem = models.ImageField(
        "Imagem",
        upload_to="personagem/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
        ordering = ["nome"]

    def __str__(self) -> str:
        return f'{self.nome} ({self.cenario.criador.username})'
