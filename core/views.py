from django.http import HttpResponse


def home(request):
    return HttpResponse("HomeHub Lite: setup complete.")
