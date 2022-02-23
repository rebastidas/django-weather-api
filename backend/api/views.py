from django.shortcuts import render
from rest_framework import status 
from rest_framework.permissions import AllowAny 
from rest_framework.views import APIView
from rest_framework.response import Response



class WeatherInfo(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'message':'Welcome to API Weather'}, status=status.HTTP_200_OK)
