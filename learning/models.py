from django.core.validators import MaxValueValidator
from django.db import models

from categoryscience.models import CategoryScience


class Article(models.Model):
    name = models.CharField(max_length=2000)
    category = models.ForeignKey(CategoryScience, on_delete=models.CASCADE, null=True, blank=True)


class Quizzes(models.Model):
    name = models.CharField(max_length=1500)
    time_to_achieve = models.DurationField()
    topic = models.ForeignKey(Article, on_delete=models.CASCADE)


class Tasks(models.Model):
    name = models.CharField(max_length=500)
    goal = models.CharField(max_length=100)
    difficulty = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    description = models.CharField(max_length=100)
    time_to_achieve = models.DurationField()
    time_achieved = models.DurationField()
    asrticle = models.ForeignKey(Article, on_delete=models.CASCADE)


class AnswersToTask(models.Model):
    task_number = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    time_achieved = models.DurationField()


class AnswerToQuizzes(models.Model):
    quizzes_number = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    time_achieved = models.DurationField()


class QuestionsToQuizzes(models.Model):
    number = models.CharField(max_length=10)
    difficulty = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    quizzes_to_answer = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
