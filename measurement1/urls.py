from django.urls import path


from measurement1.views import SensorAPIList, SensorUpAPIList, MeasurementAPIList, MeasurementUPAPIList

urlpatterns = [
    #path('sensors/', SensorView.as_view()),
    path('sensors/', SensorAPIList.as_view()),
    path('measurements/', MeasurementAPIList.as_view()),
    path('sensors/<pk>/', SensorUpAPIList.as_view()),
    path('measurements/<pk>/', MeasurementUPAPIList.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]

