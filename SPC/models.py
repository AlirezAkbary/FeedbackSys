from django.db import models
from Course.models import Course
from Student.models import Student
from Professor.models import Professor
# Create your models here.


class SPC(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

