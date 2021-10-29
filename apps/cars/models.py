from django.core import validators as V
from django.db import models

from apps.autopark.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Машины'
        verbose_name_plural = 'Машина'
        ordering = ('id',)

    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(3), V.MaxLengthValidator(
        20)])
    model = models.CharField(max_length=20)
    year = models.IntegerField(validators=[V.MinValueValidator(1980), V.MinValueValidator(2021)])
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
