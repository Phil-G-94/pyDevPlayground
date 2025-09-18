from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


# defines a fn `index` which returns the following HttpResponse
def index(request: HttpRequest) -> HttpResponse:
    """Return the latest 5 questions as a comma-separated HttpResponse."""

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")  # load template
    # context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))

    # shortcut #
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int):
    """Return a 404 error if the question can't be found"""
    # throwing 404 errors
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    # shortcut #
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of the question %s"
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on the question %s." % question_id)
