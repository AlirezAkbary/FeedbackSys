from django.shortcuts import render
from .models import Course
from .forms import CourseCreateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Professor.models import Professor
from Student.models import Student
from .models import Course
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from Question.forms import MultipleChoiceForm, LongAnswerForm
from Question.models import MultipleChoiceQuestion, Question, Choice, LongAnswerQuestion
import datetime

@login_required
def AddCourse(request, id):

    u = Professor.objects.filter(
        Q(ProfID=id)
    )
    notif_num = 0
    for i in u[0].course_set.all():
        for j in i.not_verified_students.all():
            notif_num += 1

    if request.method == "POST":### Need Checks for wrong inputs
        post_dict = dict(request.POST.lists())



        CourseForm = Course(CourseID=int(post_dict['CourseID'][0]))
        CourseForm.GroupID = int(post_dict['GroupID'][0])
        CourseForm.Name = post_dict['Name'][0]

        new_professors = post_dict['new']
        existing = []
        print(Professor.objects.all())

        for i in new_professors:
            if i != '':
                prof = Professor.objects.filter(
                    Q(ProfID=int(i))
                )
                if not prof:
                    course_form = CourseCreateForm()
                    return render(request, 'course/new_form.html', {'course_form': course_form, 'u': u[0], 'n' : notif_num, 'flag':1})

        CourseForm.save()
        self_user = Professor.objects.get(ProfID=int(request.user.username))
        CourseForm.Professor.add(self_user)


        for i in new_professors:
            if i != '':
                current_prof = get_object_or_404(Professor, ProfID=int(i))
                if current_prof is not None:
                    CourseForm.Professor.add(current_prof)
        return HttpResponseRedirect(reverse('professor', kwargs={'id':int(request.user.username)}))
    else:
        course_form = CourseCreateForm()
    return render(request, 'course/new_form.html', {'course_form':course_form, 'u': u[0],  'n' : notif_num, 'flag':0})
# Create your views here.

@login_required
def general_search(request):
    print(request.user.username)
    prof = Professor.objects.filter(
        Q(ProfID=int(request.user.username))
    )

    if len(prof) != 0:
        return search_course_professor(request)
    else:
        return search_course_student(request)


def search_course_professor(request):
    pass


def search_course_student(request):

    query = request.GET.get('q')

    user = request.user.username

    user = Student.objects.filter(
        Q(StudentID=user)
    )



    object_list = Course.objects.filter(
        Q(Name__icontains=query)
    )
    is_in = False
    for o in object_list:
        for u in o.not_verified_students.all() :
            if u.StudentID == user[0].StudentID:
                is_in = True
    print(is_in)
    professor_name_strings = []
    objects = []
    for o in object_list:
        prof = o.Professor.all()

        s = ""
        for i in range(len(prof)):
            s += prof[i].FirstName + " " + prof[i].LastName
        professor_name_strings.append(s)
    for o in range(len(object_list)):
        objects.append([object_list[o], o])

    context = {
        'object': object_list,
        'u':user[0],
        'names':professor_name_strings,
        'query' : query,
        'is_not_verified' : is_in
    }



    return render(request, 'Course/new_search.html', context)

def joinCourse(request, id, group, query):
    object = Course.objects.filter(
        Q(CourseID=id, GroupID = group)

    )
    user = request.user.username
    user = Student.objects.filter(
        Q(StudentID=user)
    )
    context = {
        "object":object[0],
        "user":user[0]
    }

    object[0].not_verified_students.add(user[0])

    print(user[0].course_set.all())
    print(object[0].Student.all())





    return HttpResponseRedirect("/./search/?q="+query)


@login_required
def courseHome(request, cid, gid):
    print(request.user.username)
    prof = Professor.objects.filter(
        Q(ProfID=int(request.user.username))
    )
    if len(prof) != 0:
        return courseHomeProfView(request, cid, gid)
    else:
        return courseHomeStudentView(request, cid, gid)


def courseHomeProfView(request, cid, gid):
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context = {}
    context['course'] = the_course
    questions = Question.objects.all()

    print("hey")
    print(len(the_course.Questions.all()))

    if len(the_course.Questions.all()) == 0:
        context['questions'], context['cid'], context['gid'] = questions, cid, gid
        context['search_flag'] = 0
        return render(request, 'professor/ProfessorCourseView.html', context)
    else:
        question_to_show = the_course.Questions.all()[0]
        return HttpResponseRedirect(reverse('general_question', kwargs={'cid': cid, 'gid': gid, 'qid':question_to_show.id}))



def courseHomeStudentView(request, cid, gid):
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context = {}
    context['course'] = the_course
    questions = Question.objects.all()

    if len(the_course.Questions.all()) == 0:
        context['questions'], context['cid'], context['gid'] = questions, cid, gid
        context['search_flag'] = 0
        return render(request, 'student/StudentCourseView.html', context)
    else:
        question_to_show = the_course.Questions.all()[0]
        return HttpResponseRedirect(reverse('general_question', kwargs={'cid': cid, 'gid': gid, 'qid':question_to_show.id}))

def StudentCourseList_view(request, cid, gid):
    the_professor = Professor.objects.get(ProfID=request.user.username)
    n_num = 0
    for i in the_professor.course_set.all():
        for j in i.not_verified_students.all():
            n_num += 1

    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context = {}
    context['course'] = the_course
    context['professor'] = the_professor
    context['n'] = n_num
    return render(request, 'professor/StudentListCoursePage.html', context)

def AddMultipleChoiceQuestion(request, cid, gid):
    if request.method == "POST":
        print("------------------------------------------------")
        print(dict(request.POST.lists()))


        post_dict = dict(request.POST.lists())

        created_question = MultipleChoiceQuestion(title=post_dict['title'][0])
        created_question.Date = datetime.datetime.now()
        created_question.q_type = 'M'
        created_question.subject = post_dict['subject'][0]
        created_question.save()

        choices = post_dict['new']
        for i in choices:
            if i != '':
                created_choice = Choice(text=i, question=created_question)
                created_choice.save()

        the_course = Course.objects.get(CourseID=cid, GroupID=gid)
        the_course.Questions.add(created_question)
        return HttpResponseRedirect(reverse('MultChoiceQ', kwargs={'cid':cid, 'gid':gid}))
    else:
        question_form = MultipleChoiceForm()
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    questions = Question.objects.all()
    return render(request, 'course/AddMultChoiceQ.html', {'question_form': question_form, 'course':the_course, 'questions':questions})


def AddLongAnswerQuestion(request, cid, gid):
    if request.method == "POST":
        print("------------------------------------------------")
        print(dict(request.POST.lists()))

        post_dict = dict(request.POST.lists())
        created_question = LongAnswerQuestion(title=post_dict['title'][0])

        created_question.q_type = 'L'
        created_question.Date = datetime.datetime.now()
        created_question.subject = post_dict['subject'][0]

        created_question.save()
        the_course = Course.objects.get(CourseID=cid, GroupID=gid)
        the_course.Questions.add(created_question)
        return HttpResponseRedirect(reverse('LongAnswerQ', kwargs={'cid': cid, 'gid': gid}))
    else:
        question_form = LongAnswerForm()

    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    questions = Question.objects.all()
    return render(request, 'course/AddLongAnswerQ.html', {'question_form': question_form, 'course':the_course, 'questions':questions})