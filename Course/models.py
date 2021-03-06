from django.db import models
from Professor.models import Professor
from Student.models import Student as St
from Question.models import Question
# Create your models here.

StatusChoices = [('active', 'active'), ('archived', 'archived')]
class Course(models.Model):
    CourseID = models.PositiveIntegerField(null=False, blank=False)
    GroupID = models.PositiveSmallIntegerField(null=False, blank=False)
    Name = models.CharField(null=False, blank=False, max_length=100)
    Professor = models.ManyToManyField(Professor, blank=False)
    Student = models.ManyToManyField(St, blank=False)
    not_verified_students = models.ManyToManyField(St, blank=False, related_name='not_verified')
    Questions = models.ManyToManyField(Question,  blank=True)
    Status = models.CharField(max_length=20, null=True, blank=False, choices=StatusChoices, default='active')

    class Meta:
        ordering = ['CourseID']
        unique_together = (('CourseID', 'GroupID'),)

