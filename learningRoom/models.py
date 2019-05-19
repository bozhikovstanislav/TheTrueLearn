from django.db import models

from categoryscience.models import CategoryScience


class RoomQuizze(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(CategoryScience, on_delete=models.CASCADE)
