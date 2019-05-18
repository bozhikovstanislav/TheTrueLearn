from django.db import models


class Quizzes(models.Model):
    name = models.CharField(max_length=1500)
    pass


class Tasks(models.Model):
    pass


class Answers(models.Model):
    pass


class Article(models.Model):
    name = models.CharField(max_length=2000)
    pass

