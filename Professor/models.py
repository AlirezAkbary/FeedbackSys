from django.db import models
from User.models import *
# Create your models here.


class Professor(UserProfile):
    ProfID = models.PositiveIntegerField(null=False, blank=False)
    Degree = models.CharField(null=False, blank=False, max_length=100)
    Field = models.CharField(null=False, blank=False, max_length=100)