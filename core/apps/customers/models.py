from django.db import models

from core.apps.common.models import TimedBaseModel


class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name="Phone number",
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name="User token",
        max_length=255,
        unique=True,
    )

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
