from django.contrib import admin

# Register your models here.
from .models import Article,Quizzes,QuestionsToQuizzes,AnswerToQuizzes,AnswersToTask,Tasks

admin.site.register(Article)
admin.site.register(Quizzes)
admin.site.register(QuestionsToQuizzes)
admin.site.register(AnswerToQuizzes)
admin.site.register(AnswersToTask)
admin.site.register(Tasks)
