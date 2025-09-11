from django.http import HttpRequest, HttpResponse

# defines a fn `index` which returns the following HttpResponse
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World. You're at the polls index.")
