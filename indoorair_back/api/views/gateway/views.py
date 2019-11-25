from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, response

from api.serializers.gateway import RegisterSerializer, LoginSerializer


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )



class LoginAPI(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={
            'request': request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'details': 'You have been logged in successfully!'
            },
        )


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })
