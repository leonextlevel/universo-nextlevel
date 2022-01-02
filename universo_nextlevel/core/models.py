from django.db import models
from django.conf import settings


class Cenario(models.Model):
    imagem = models.ImageField(
        "Imagem",
        upload_to="cenario/",
        null=True,
        blank=True,
    )
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=64)
    data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)

    class Meta:
        verbose_name = 'Cenário'
        verbose_name_plural = 'Cenários'
        ordering = ['nome', 'data_criacao']

    def __str__(self) -> str:
        return self.nome
