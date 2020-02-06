from django.db import models
from User.models import *
from Question.models import Choice, Answer
# Create your models here.


class Student(UserProfile):
    StudentID = models.PositiveIntegerField(null=False, blank=False)
    degree = models.CharField(null=False, blank=False, max_length=100)
    SelectedChoices = models.ManyToManyField(Choice, null=True, blank=True)
    LongAnswers = models.ManyToManyField(Answer, null=True, blank=True)

