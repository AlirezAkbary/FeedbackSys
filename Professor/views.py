from django.shortcuts import render
from .models import Professor
from Course.models import Course
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def professor_view(request, id):
    obj = Professor.objects.get(ProfID=id)

    context = {
        "object" : obj
    }
    return render(request, "professor/New_HomeProfPage.html", context)

@login_required
def archiveCourseProfessor_view(request, id):
    obj = Professor.objects.get(ProfID=id)

    context = {
        "object" : obj
    }
    return render(request, "professor/archiveCourseProfPage.html", context)
@login_required
def professorDeleteCourse_view(request, cid, gid):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)
    course = Course.objects.filter(
        Q(CourseID=cid, GroupID=gid)
    )
    print(id)
    print(cid)

    course[0].Professor.remove(prof)
    context = {
        "object" : prof
    }
    return render(request, "professor/New_HomeProfPage.html", context)
# Create your views here.
@login_required
def professorArchiveCourse_view(request, cid, gid):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)
    Course.objects.filter(
        Q(CourseID=cid, GroupID=gid)
    ).update(Status='archive')
    context = {
        "object": prof
    }
    return render(request, "professor/New_HomeProfPage.html", context)


