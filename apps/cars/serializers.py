from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        extra_kwargs = {
            'autopark': {'read_only': True},
        }

    # def validate(self, data):
    #     if data.get('model') == data.get('brand'):
    #         raise serializers.ValidationError('Error model is equal brand')
    #     return data
    def validate_year(self, year):
        if year == 2005:
            raise serializers.ValidationError('Error 2005')
        return year


class Car2Serializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand')
