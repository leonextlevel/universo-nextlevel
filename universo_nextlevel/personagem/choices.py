from django.db import models


class SexoChoices(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMININO = 'F', 'Feminino'
    INDEFINIDO = 'I', 'Indefinido'

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