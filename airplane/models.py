from django.db import models
from django.core import validators as V


# Create your models here.
class AirPlaneModel(models.Model):
    class Meta:
        db_table = 'airplane'

    name = models.CharField(max_length=20,
                            validators=[V.RegexValidator('^[a-zA-Z]{2,20}$', 'name must be 2-20 characters')]
                            )
    speed = models.IntegerField(validators=[V.MinValueValidator(200), V.MaxValueValidator(1000)])
    engine = models.FloatField(validators=[V.MinValueValidator(2), V.MaxValueValidator(6)])
