from django.db import models


class Personagem(models.Model):

    class SexoChoices(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    class TendenciaChoices(models.TextChoices):
        LEAL_BOM = 'LB', 'Leal e Bom'
        NEUTRO_BOM = 'NB', 'Neutro e Bom'
        CAOTICO_BOM = 'CB', 'Caótico e Bom'
        LEAL_NEUTRO = 'LN', 'Leal e Neutro'
        NEUTRO = 'N', 'Neutro'
        CAOTICO_NEUTRO = 'CN', 'Caótico e Neutro'
        LEAL_MAU = 'LM', 'Leal e Mau'
        NEUTRO_MAU = 'NM', 'Neutro e Mau'
        CAOTICO_MAU = 'CM', 'Caótico e Mau'

    nome = models.CharField(max_length=100)
    idade = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=1, choices=SexoChoices.choices)
    profissao = models.CharField("Profissão", max_length=50)
    caracteristica_marcante = models.TextField("Característica Marcante")
    background = models.TextField()
    tendencia = models.CharField(
        "Tendência",
        max_length=2,
        choices=TendenciaChoices.choices,
    )
    descricao_fisica = models.TextField("Descrição Física")
    imagem_perfil = models.ImageField(
        "Imagem de Perfil",
        upload_to="personagem/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome
