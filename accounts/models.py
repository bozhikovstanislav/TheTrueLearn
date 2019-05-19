from django.contrib.auth.models import User
from django.db import models

from institutions.models import Institution
from learning.models import Quizzes, Tasks
from profession.models import Profession


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE,null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,null=True, blank=True)
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE, null=True, blank=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Student(Person, models.Model):
    def __init__(self, user, profession, institution, quizzes, tasks):
        Person.__init__(user=user, profession=profession, institution=institution, quizzes=quizzes, tasks=tasks)

    def __str__(self):
        return f"{self.user}"


class Teacher(Person, models.Model):
    def __init__(self, user, profession, institution, quizzes, tasks):
        Person.__init__(self,user=user, profession=profession, institution=institution, quizzes=quizzes, tasks=tasks)

    def __str__(self):
        return f"{self.user}"
