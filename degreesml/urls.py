from django.urls import path
from .views import convertTemperature

urlpatterns = [
    path('convertir_temperatura/', convertTemperature.as_view(), name='convertir_temperatura'),
]