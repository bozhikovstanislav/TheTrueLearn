from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    number_of_employee=models.PositiveIntegerField()
