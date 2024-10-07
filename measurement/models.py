from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='meas')
    temperature = models.BigIntegerField()
    date_time = models.DateTimeField()

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
