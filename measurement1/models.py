from django.db import models


class Sensor1(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)


class Measurement1(models.Model):
    sensor = models.ForeignKey(Sensor1, on_delete=models.CASCADE, related_name='meas')
    temperature = models.CharField(max_length=256)
    date_time = models.DateTimeField(auto_now_add=True)

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

