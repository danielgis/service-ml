
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from .ml_model import ml_model

class convertTemperature(APIView):
    def post(self, request):
        celsius = request.data.get("celsius")
        
        if celsius is None:
            return Response({"error": "Se debe proporcionar la temperatura en Celsius."}, status=status.HTTP_400_BAD_REQUEST)
        
        celsius_array = np.array([celsius], dtype=float)
        fahrenheit = ml_model.model_ml.predict(celsius_array)

        return Response({"celsius": celsius, "fahrenheit": fahrenheit[0][0]}, status=status.HTTP_200_OK)