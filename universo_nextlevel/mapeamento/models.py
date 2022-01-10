from django.db import models

from .choices import TipoDistritoChoices

from universo_nextlevel.core.models import Cenario


class Nacao(models.Model):
    cenario = models.ForeignKey(Cenario, on_delete=models.CASCADE, verbose_name="Cenário")
    nome = models.CharField('Nome', max_length=32)

    class Meta:
        verbose_name = 'Nação'
        verbose_name_plural = 'Nações'
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome


class Estado(models.Model):
    cenario = models.ForeignKey(Cenario, on_delete=models.CASCADE, verbose_name="Cenário")
    nome = models.CharField('Nome', max_length=32)
    dono = models.ForeignKey(Nacao, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome


class Distrito(models.Model):
    cenario = models.ForeignKey(Cenario, on_delete=models.CASCADE, verbose_name="Cenário")
    nome = models.CharField('Nome', max_length=32)
    tipo = models.CharField('Tipo', max_length=9, choices=TipoDistritoChoices.choices)
    dono = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome
