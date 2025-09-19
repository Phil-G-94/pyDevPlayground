from typing import List
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# namespacing URL names
# prevents name collisions
# across different python modules that might share the same view names
# i.e. `index` | `detail`
app_name = "polls"

# define url patterns for the polls app
urlpatterns: List[URLPattern] = [
    path(
        "", views.index, name="index"
    ),  # defines a url `index` and maps it against the index fn defined in views.py
    path(
        "<int:question_id>/", views.detail, name="detail"
    ),  # the 'name' value as called by the {% url %} template tag within the corresponding template
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
