
import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement1.models import Sensor1, Measurement1
from measurement1.serializers import SensorSerializer, MeasurementSerializer
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor1.objects.all()
    serializer_class = SensorSerializer

class SensorUpAPIList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor1.objects.all()
    serializer_class = SensorSerializer

class MeasurementAPIList(generics.ListCreateAPIView):
    queryset = Measurement1.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementUPAPIList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement1.objects.all()
    serializer_class = MeasurementSerializer

class SensorOneAPIList(generics.ListCreateAPIView):
    queryset = Sensor1.objects.all()
    serializer_class = SensorSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы: