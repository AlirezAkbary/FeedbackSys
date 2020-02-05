from django.shortcuts import render
from Course.models import Course
from .models import Question, Choice, MultipleChoiceQuestion
from django.contrib.auth.decorators import login_required
from Professor.models import Professor
from Student.models import Student
from django.db.models import Q
from .models import MultipleChoiceQuestion
# Create your views here.
@login_required
def question_view_general(request, cid, gid, qid):
    prof = Professor.objects.filter(
        Q(ProfID=int(request.user.username))
    )

    if len(prof) != 0:
        return question_view_professsor(request, cid, gid, qid)
    else:
        return question_view_student(request,cid, gid, qid)


def question_view_student(request, cid, gid, qid):


    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context = {}
    context['course'] = the_course
    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid
    the_question = Question.objects.get(id=qid)

    #print(type(the_question))


    if the_question.q_type == 'M':
        the_question = MultipleChoiceQuestion.objects.get(id=qid)
        context['the_question'] = the_question
        return render(request, 'student/QuestionMultipleStudentPage.html', context)
    else:
        pass



def question_view_professsor(request, cid, gid, qid):
    pass
