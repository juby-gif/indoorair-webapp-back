from django.shortcuts import get_object_or_404
from rest_framework import status, response, views

from foundation.models import Sensor
from api.serializers.sensor import SensorRetrieveSerializer


class SensorRetrieveAPI(views.APIView):
    def get(self, request, id):
        sensor = get_object_or_404(Sensor, id=int(id))
        serializer = SensorRetrieveSerializer(sensor)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
