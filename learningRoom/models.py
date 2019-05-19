from django.db import models

from categoryscience.models import CategoryScience
from common.models import ParticipantListener, ParticipantLecturer
from learning.models import Article, Quizzes


class RoomQuizze(models.Model):
    name = models.CharField(max_length=500)
    category = models.OneToOneField(CategoryScience, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    participantLecturer = models.OneToOneField(ParticipantLecturer, on_delete=models.CASCADE)
    participantListener = models.ForeignKey(ParticipantListener, on_delete=models.CASCADE)
