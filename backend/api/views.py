import requests
import json
import codecs
from django.conf import settings
from django.shortcuts import render
from rest_framework import status 
from rest_framework.permissions import AllowAny 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CityWeather
from .serializer import SerializerCityWeather

from .utils.average import average_weather


class WeatherInfo(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            url = f'{settings.URL_API}weather?q={data["city"]}&appid={settings.API_KEY}'
            r=requests.get(url)
            if(r.status_code==404):
                return Response({'menssage':'Esa ciudad no existe'}, status=r.status_code)
            result=json.loads(r.text.encode('utf-8'))
            if CityWeather.objects.filter(city_code = result['id']).exists():
                avg = average_weather(result['coord']['lon'],result['coord']['lat'])
                CityWeather.objects.filter(city_code = result['id']).update(averagetemp = avg)
                temp=CityWeather.objects.get(city_code = result['id'])
                return Response({'result':SerializerCityWeather(temp).data}, status=status.HTTP_200_OK)
            avg = average_weather(result['coord']['lon'],result['coord']['lat'])
            c=CityWeather(
                cityname = result['name'],
                currentemp = result['main']['temp'],
                fellslike = result['main']['feels_like'],
                averagetemp = avg,
                citylat = result['coord']['lat'],
                citylon = result['coord']['lon'],
                city_code = result['id']
            )
            c.save()
            return Response({'result':SerializerCityWeather(c).data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'Error':'Ups al parecer hubo un error...'}, status=status.HTTP_400_BAD_REQUEST)

#docker run -d --name postgres_weather_api -e POSTGRES_USER=weather_api_user -e POSTGRES_PASSWORD=weather_api_pass -e POSTGRES_DB=weather_api_db -p 5432:5432 postgres