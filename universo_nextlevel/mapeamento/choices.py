from django.db import models


class TipoDistritoChoices(models.TextChoices):
    METROPOLE = 'metropole', 'Metrópole'
    CIDADE = 'cidade', 'Cidade'
    VILA = 'vila', 'Vila'
