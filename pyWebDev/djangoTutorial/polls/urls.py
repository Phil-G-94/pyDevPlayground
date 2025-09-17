from typing import List
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: List[URLPattern] = [
    path(
        "", views.index, name="index"
    ),  # defines a url `index` and maps it against the index fn defined in views.py
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
