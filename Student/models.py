from django.db import models
from User.models import *

# Create your models here.


class Student(UserProfile):
    StudentID = models.PositiveIntegerField(null=False, blank=False)
    degree = models.CharField(null=False, blank=False, max_length=100)

