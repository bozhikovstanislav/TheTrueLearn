from django.contrib import admin

from .models import Tasks,Quizzes,Article,AnswersToTask,AnswerToQuizzes,QuestionsToQuizzes


admin.site.register(Tasks)
admin.site.register(Quizzes)
admin.site.register(Article)
admin.site.register(AnswersToTask)
admin.site.register(AnswerToQuizzes)
admin.site.register(QuestionsToQuizzes)
