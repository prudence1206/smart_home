import json

import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorAPIList(generics. ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(APIView):
     #def get(self, request):
     #    sensors = Sensor.objects.all()
     #    print(sensors)
     #    ser = SensorSerializer(sensors, many=True)
     #    #return Response(ser.data)
     #    return Response(ser)

     def post(self, request):
         data = json.loads(request.body)
         print(data['name'])
         a = Sensor(name=data['name'],description=data['description']).save()
         ser = Sensor.objects.all()
         for s in ser:
             print(s.name)
         return Response({'status': 'OK'})

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы: