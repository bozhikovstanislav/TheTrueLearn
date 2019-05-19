from django.db import models

from accounts.models import Student, Teacher


class ParticipantLecturer(models.Model):
    id_student = models.ManyToManyField(Student)
    id_teacher = models.ManyToManyField(Teacher)


class ParticipantListener(models.Model):
    id_student = models.ManyToManyField(Student)
    id_teacher = models.ManyToManyField(Teacher)
