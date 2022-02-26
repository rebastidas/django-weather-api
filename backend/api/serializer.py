from dataclasses import fields
from rest_framework import serializers
from .models import CityWeather

class SerializerCityWeather(serializers.ModelSerializer):
    class Meta:
        model = CityWeather
        fields = ('currentemp', 'averagetemp')