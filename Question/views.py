from django.shortcuts import render
from Course.models import Course
from .models import Question, Choice, MultipleChoiceQuestion
from django.contrib.auth.decorators import login_required
from Professor.models import Professor
from Student.models import Student
from django.db.models import Q
from .models import MultipleChoiceQuestion, Choice, LongAnswerQuestion, Answer
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
    the_question = Question.objects.get(id=qid)
    if the_question.q_type == 'M':
        return multiple_question_view_student(request, cid, gid, qid)
    return long_question_view_student(request, cid, gid, qid)


def check_choice_status(request, qid):
    the_student = Student.objects.get(StudentID=request.user.username)

    the_selected_answers = the_student.SelectedChoices
    the_question_choices = Choice.objects.filter(Q(question=qid))

    for i in the_question_choices:
        for j in the_selected_answers.all():
            if i.id == j.id:

                return i.id

    return -1


def multiple_question_view_student(request, cid, gid, qid):
    context = {}
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context['course'] = the_course

    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid



    if request.method == "POST":
        post_dict = dict(request.POST.lists())

        selected_choice = Choice.objects.get(id= post_dict['question'][0])

        the_student = Student.objects.get(StudentID=request.user.username)
        the_student.SelectedChoices.add(selected_choice)
        print(selected_choice.count)
        Choice.objects.filter(Q(id=post_dict['question'][0])).update(count=selected_choice.count + 1)
        print(selected_choice.count)

    answer_status = check_choice_status(request, qid)
    context['answer_status'] = answer_status
    if answer_status != -1:
        context['answer'] = Choice.objects.get(id=answer_status)
    the_question = MultipleChoiceQuestion.objects.get(id=qid)
    context['the_question'] = the_question

    return render(request, 'student/QuestionMultipleStudentPage.html', context)


def check_answer_status(request, qid):
    the_student = Student.objects.get(StudentID=request.user.username)

    the_answer = the_student.LongAnswers
    print(len(the_answer.all()))
    the_student_answer = Answer.objects.filter(Q(question=qid))
    #print(len(the_answer), len(the_student_answer))
    print("adfdsafd;sfhdsa;")
    if the_answer == None or len(the_student_answer) == 0:
        return -1

    for i in the_answer.all():
        for j in the_student_answer:
            print(i.id, j.id)
            if i.id == j.id:
                return i.id

    return -1


def long_question_view_student(request, cid, gid, qid):
    context = {}
    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context['course'] = the_course

    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid

    the_question = LongAnswerQuestion.objects.get(id=qid)
    context['the_question'] = the_question

    if request.method == "POST":
        post_dict = dict(request.POST.lists())
        print(post_dict)
        answerForm = Answer(question=the_question)
        answerForm.text = post_dict['answer'][0]
        answerForm.save()
        the_student = Student.objects.get(StudentID=request.user.username)
        the_student.LongAnswers.add(answerForm)
        pass

    answer_status = check_answer_status(request, qid)
    context['answer_status'] = answer_status
    if answer_status != -1:
        context['answer'] = Answer.objects.get(id=answer_status)

    return render(request, 'student/QuestionLongStudentPage.html', context)



def question_view_professsor(request, cid, gid, qid):
    the_question = Question.objects.get(id=qid)
    if the_question.q_type == 'M':
        return multiple_question_view_professor(request, cid, gid, qid)
    return long_question_view_professor(request, cid, gid, qid)


def multiple_question_view_professor(request, cid, gid, qid):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid

    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context['course'] = the_course

    the_question = MultipleChoiceQuestion.objects.filter(Q(id=qid))
    context['the_question'] = the_question[0]

    sum_of_count = 0
    for i in the_question[0].choices.all():
        sum_of_count += i.count
    if sum_of_count != 0:
        context['total_count'] = sum_of_count
    else:
        context['total_count'] = 1
    context['total_count'] /= 100
    return render(request, 'professor/QuestionMultipleProfessorPage.html', context)


def long_question_view_professor(request, cid, gid, qid):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    context['qid'], context['cid'], context['gid'] = qid, cid, gid

    the_course = Course.objects.get(CourseID=cid, GroupID=gid)
    context['course'] = the_course

    the_question = LongAnswerQuestion.objects.filter(Q(id=qid))
    context['the_question'] = the_question[0]

    return render(request, 'professor/QuestionLongProfessorPage.html', context)

