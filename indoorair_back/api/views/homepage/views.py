from rest_framework import status, response, views


class VersionAPI(views.APIView):
    def get(self,request):
        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'version' : '3',
            }
        )
