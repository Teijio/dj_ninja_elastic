from django.db import models

from core.apps.common.models import TimedBaseModel


class Product(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название товара",
        max_length=255,
    )
    description = models.TextField(
        blank=True,
    )
