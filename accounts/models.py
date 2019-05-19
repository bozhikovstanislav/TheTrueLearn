from django.contrib.auth.models import User
from django.db import models

from institutions.models import Institution
from learning.models import Quizzes, Tasks
from profession.models import Profession


class People(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE, null=True, blank=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True, blank=True)


class Student(People, models.Model):
    pass


class Teacher(People, models.Model):
    pass
