from django.db import models
from django.core import validators as V

# Create your models here.

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Машины'
        verbose_name_plural = 'Машина'


    brand = models.CharField(max_length=20, validators=[V.MinLengthValidator(3), V.MaxLengthValidator(20)])   # unique=True, null=True, default='AUDI' blank=True)
    model = models.CharField(max_length=20)
    year = models.IntegerField(validators=[V.MinValueValidator(1980), V.MinValueValidator(2021)])

    def __str__(self):
        return self.brand
