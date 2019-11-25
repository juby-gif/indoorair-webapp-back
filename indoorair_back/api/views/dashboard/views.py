from rest_framework import response, views, status

from foundation.models import Instrument
from api.serializers.dashboard import DashboardSerializer


class DashboardAPI(views.APIView):
    def get(self, request):
        instruments = Instrument.objects.filter(user=request.user)
        serializer = DashboardSerializer(instruments)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
