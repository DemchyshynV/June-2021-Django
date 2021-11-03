import django_filters as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('year', 'gt')
    park_name = filters.CharFilter('autopark', 'name__istartswith')

    class Meta:
        model = CarModel
        fields = ('year_gt', 'park_name', 'year', 'model')
