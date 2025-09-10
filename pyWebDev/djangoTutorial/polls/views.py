from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")


def hello_world(str: str) -> str:
    return str
