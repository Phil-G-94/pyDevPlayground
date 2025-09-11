from typing import List
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: List[URLPattern] = [
    # defines a url `index` and maps it against the index fn defined in views.py
    path("", views.index, name="index")
]