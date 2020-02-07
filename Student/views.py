from django.shortcuts import render
from .models import Student
from Course.models import Course
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required
def student_view(request, id):
    print(type(id))
    obj = Student.objects.get(StudentID=id)
    context = {
        "object" : obj
    }
    print("hey")
    for i in obj.course_set.all():
        print(i.Name, i.Status)
    return render(request, "student/New_HomeStudentPage.html", context)

def student_requested_courses_view(request, id):
    obj = Student.objects.get(StudentID=id)
    context = {
        "object": obj
    }
    for i in obj.not_verified.all():
        print(i.Name, i.Status)
    return render(request, "student/requested_courses.html", context)

def archiveCourseStudent_view(request, id):
    obj = Student.objects.get(StudentID=id)

    courses = Course.objects.filter(
        Q(Status='archive')
    )
    context = {
        "object": courses,
        "u": obj
    }
    return render(request, "student/student_archived.html", context)




