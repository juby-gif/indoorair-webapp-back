from django.http import HttpResponse, JsonResponse


def get_profile_retrieve_api(request):
    return JsonResponse({
         'first_name': request.user.first_name,
         'last_name': request.user.last_name,
         'email': request.user.email,
         'username': request.user.username,
    })

def post_profile_update_api(request):
    return JsonResponse({
         'version': '1.0',
    })
