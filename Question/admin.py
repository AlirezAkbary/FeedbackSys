from django.contrib import admin
from Question.models import *
# Register your models here.
admin.site.register(MultipleChoiceQuestion)
admin.site.register(LongAnswerQuestion)
admin.site.register(Choice)