from django.urls import path

from measurement.models import Sensor
from measurement.views import SensorView, SensorAPIList

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/', SensorAPIList.as_view()),
    #path('weapon/<pk>/', WeaponView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
