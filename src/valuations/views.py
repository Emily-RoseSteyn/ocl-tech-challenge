from django.http import HttpResponse


def index(request):
    if request.method == "GET":
        return HttpResponse("Not implemented yet")
    else:
        return HttpResponse("Hello, world. You're at the valuations index.")
