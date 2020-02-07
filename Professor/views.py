from django.shortcuts import render, HttpResponseRedirect
from .models import Professor
from Course.models import Course
from Student.models import Student
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def professor_view(request, id):
    obj = Professor.objects.get(ProfID=id)
    notif_num = 0
    for i in obj.course_set.all():
        for j in i.not_verified_students.all():
            notif_num += 1
    context = {
        "object" : obj,
        "n" : notif_num
    }
    return render(request, "professor/New_HomeProfPage.html", context)


# @login_required
# def professor_view(request, id):
#     obj = Professor.objects.get(ProfID=id)
#     context = {
#         "object" : obj
#     }
#     return render(request, "course/AddMultChoiceQ.html", context)

@login_required
def archiveCourseProfessor_view(request, id):
    obj = Professor.objects.get(ProfID=id)
    notif_num = 0
    for i in obj.course_set.all():
        for j in i.not_verified_students.all():
            notif_num += 1


    context = {
        "object" : obj,
        "n": notif_num
    }
    return render(request, "professor/archiveCourseProfPage.html", context)
@login_required
def professorDeleteCourse_view(request, cid, gid):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)
    course = Course.objects.filter(
        Q(CourseID=cid, GroupID=gid)
    )
    print(len(course))
    print(id)
    print(cid)
    print(gid)

    course[0].delete()
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


def professor_notifications(request, id):
    prof = Professor.objects.get(ProfID=id)
    notif_num = 0
    for i in prof.course_set.all():
        for j in i.not_verified_students.all():
            notif_num += 1
    context = {
        "object": prof,
        "n": notif_num
    }
    return render(request, "professor/notifs.html", context)

def prof_add_student(request, cid, gid, sid):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)
    student = Student.objects.get(StudentID=sid)
    course = Course.objects.filter(
        Q(CourseID=cid, GroupID=gid)
    )
    course[0].not_verified_students.remove(student)
    course[0].Student.add(student)
    context = {
        "object": prof
    }
    url = "/./notifications/" + id
    return HttpResponseRedirect(url)

def prof_reject_student(request, cid, gid, sid):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)
    student = Student.objects.get(StudentID=sid)
    course = Course.objects.filter(
        Q(CourseID=cid, GroupID=gid)
    )
    course[0].not_verified_students.remove(student)


    context = {
        "object": prof
    }
    url = "/./notifications/" + id
    return HttpResponseRedirect(url)

def verify_all(request):
    id = request.user.username
    prof = Professor.objects.get(ProfID=id)

    for j in prof.course_set.all():
        for i in j.not_verified_students.all():
            j.Student.add(i)
            j.not_verified_students.remove(i)



    url = "/./notifications/" + id
    return HttpResponseRedirect(url)



