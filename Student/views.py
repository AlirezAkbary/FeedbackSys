from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def student_view(request, id):
    print(type(id))
    obj = Student.objects.get(StudentID=id)
    context = {
        "object" : obj
    }
    return render(request, "student/detstu.html", context)
