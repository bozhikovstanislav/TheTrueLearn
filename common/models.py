from django.db import models

from accounts.models import Student, Teacher


class ParticipantLecturer(models.Model):
    id_student = models.ManyToManyField(Student, null=True, blank=True)
    id_teacher = models.ManyToManyField(Teacher, null=True, blank=True)


class ParticipantListener(models.Model):
    id_student = models.ManyToManyField(Student, null=True, blank=True)
    id_teacher = models.ManyToManyField(Teacher, null=True, blank=True)
