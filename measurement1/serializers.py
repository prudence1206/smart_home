from rest_framework import serializers
from measurement1.models import Sensor1, Measurement1


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor1
        fields = "__all__"

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement1
        fields = '__all__'



# TODO: опишите необходимые сериализаторы

