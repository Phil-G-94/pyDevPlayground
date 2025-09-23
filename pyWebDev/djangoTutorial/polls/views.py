from django.db.models import F
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Each generic view needs to know the model it's acting on - defined by


class HomeView(generic.TemplateView):
    template_name = "home.html"


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """Submit vote. Redirect if successful, throw exception if choice doesn't exist"""
    question: Question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice: Choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice"},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# views - the hard way #
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse

# from .models import Question, Choice
# from django.db.models import F

# # defines a fn `index` which returns the following HttpResponse
# def index(request: HttpRequest) -> HttpResponse:
#     """Return the latest 5 questions as a comma-separated HttpResponse."""

#     # latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")  # load template
#     # context = {"latest_question_list": latest_question_list}
#     # return HttpResponse(template.render(context, request))

#     # shortcut #
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)


# def detail(request: HttpRequest, question_id: int):
#     """Return a 404 error if the question can't be found"""
#     # throwing 404 errors
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {"question": question})

#     # shortcut #
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# def vote(request: HttpRequest, question_id: int) -> HttpResponse:
#     """Submit vote. Redirect if successful, throw exception if choice doesn't exist"""
#     question: Question = get_object_or_404(Question, pk=question_id)

#     try:
#         selected_choice: Choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(
#             request,
#             "polls/detail.html",
#             {"question": question, "error_message": "You didn't select a choice"},
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()

#     return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# def results(request: HttpRequest, question_id: int):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
