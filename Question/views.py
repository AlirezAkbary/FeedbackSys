from django.shortcuts import render
from Course.models import Course
from .models import Question
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def QuestionView(request, cid, gid, qid):
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context = {}
    context['course'] = the_course
    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid
    return render(request, 'question/QuestionPage.html', context)
