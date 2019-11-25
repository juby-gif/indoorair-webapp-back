from foundation.models import Instrument
from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse

from api.serializers.instrument import InstrumentRetrieveSerializer


def get_instruments_list_api(request):
    instruments = Instrument.objects.filter(user=request.user)
    output = []
    for instrument in instruments.all():
        output.append({
            'id': instrument.id,
            'name': instrument.name,
        })
    return JsonResponse({
        'instruments': output
    })

class InstrumentRetrieveAPI(views.APIView):
    def get(self, request, id):
        instrument = Instrument.objects.get(id=int(id))
        serializer = InstrumentRetrieveSerializer(instrument, many=False)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

class InstrumentUpdateAPI(views.APIView):
    def put(self, request, id):
        instrument = Instrument.objects.get(id=id)
        serializer = InstrumentUpdateSerializer(instrument, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updated instrument'
            }
        )
