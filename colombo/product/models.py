from decimal import Decimal
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        validators=[MinLengthValidator(5)],
        max_length=255
    )
    price = models.DecimalField(
        validators=[MinValueValidator(Decimal('0.01'))],
        decimal_places=2,
        max_digits=20,
    )
    description = models.CharField(
        validators=[MinLengthValidator(10)],
        max_length=255,
        null=True,
        blank=True
    )
    in_stock = models.BooleanField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return self.name
