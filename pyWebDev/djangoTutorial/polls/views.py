from django.http import HttpRequest, HttpResponse


# defines a fn `index` which returns the following HttpResponse
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World. You're at the polls index.")


def detail(request: HttpRequest, question_id: int):
    return HttpResponse("You're looking at the question %s." % question_id)


def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of the question %s"
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on the question %s." % question_id)
