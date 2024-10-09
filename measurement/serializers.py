from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    model = Sensor
    fields = [id, model.name, model.description]

class MeasurementSerializer(serializers.ModelSerializer):
    model = Measurement
    fields = [model.sensor, model.date_time, model.temperature]



# TODO: опишите необходимые сериализаторы
