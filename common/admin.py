from django.contrib import admin

# Register your models here.

from .models import ParticipantLecturer,ParticipantListener

admin.site.register(ParticipantLecturer)
admin.site.register(ParticipantListener)