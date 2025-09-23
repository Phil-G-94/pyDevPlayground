# DB models

import datetime
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from typing import Optional


class Question(models.Model):
    question_text: models.CharField = models.CharField(max_length=200)
    pub_date: models.DateTimeField = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> datetime.date:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # type hint for Mypy
    choice_set: "QuerySet[Choice]"
    id: Optional[int]  # for Mypy only


class Choice(models.Model):
    question: models.ForeignKey["Question"] = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )
    choice_text: models.CharField = models.CharField(max_length=200)
    votes: models.IntegerField = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
