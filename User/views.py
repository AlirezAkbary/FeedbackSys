from django.shortcuts import render
from Student.forms import UserSignUpForm, StudentSignUpForm
from Professor.forms import ProfessorSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import EmailMessage
from Professor.models import Professor
from Student.models import Student
from User.models import UserProfile
import copy
import json
import random

# Create your views here.


def signup(request):

    registered = False
    a = copy.deepcopy(str(request.body))
    #print(a)
    flag = False
    needed_id = ""
    if request.method == 'POST':

        print(request.method, "akbar")

        if a.find("\x46\x69\x65\x6c\x64") != -1 or a.find("Field") != -1:
            user_form = UserSignUpForm(data=request.POST)
            prof_form = ProfessorSignUpForm(data=request.POST)
            profile_form = StudentSignUpForm()
            if user_form.is_valid() and prof_form.is_valid():
                flag = True
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = prof_form.save(commit=False)
                profile.user = user
                profile.ProfID = user.username
                needed_id = str(user.username)
                subject = 'Thank you for your registertion - Kondor Team'
                randomCode = str(random.randint(10000000, 99999999))
                message = 'Verfication Code : ' + randomCode
                toEmailList = user.email

                email = EmailMessage(
                        subject, message, to=[toEmailList]
                )
                email.send()
                if 'profile_pic' in request.FILES:
                    #print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.Activated = False
                profile.VerifyCode = randomCode
                profile.save()
                registered = True
            else:
                pass
                #print(user_form.errors, prof_form.errors)

        else:
            print(request.method, "amrez")
            #print(request.FILES)
            user_form = UserSignUpForm(data=request.POST)
            profile_form = StudentSignUpForm(data=request.POST)
            prof_form = ProfessorSignUpForm()
            if user_form.is_valid() and profile_form.is_valid():
                flag=True
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.StudentID = user.username
                needed_id = str(user.username)

                subject = 'Thank you for your registertion - Kondor Team'
                randomCode = str(random.randint(10000000, 99999999))
                message = 'Verfication Code : ' + randomCode
                toEmailList = user.email

                email = EmailMessage(
                        subject, message, to=[toEmailList]
                )
                email.send()

                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

                profile.Activated = False
                profile.VerifyCode = randomCode
                profile.save()
                registered = True
            else:
                pass
                #print(user_form.errors, profile_form.errors)

    else:
        user_form = UserSignUpForm()
        profile_form = StudentSignUpForm()
        prof_form = ProfessorSignUpForm()


    print("AWLIIIII", registered, flag)
    #return HttpResponse("user logged in")
    if flag:
        return HttpResponseRedirect(reverse('verification', kwargs={'id':needed_id}))
        #return render(request,'VerificationPage.html',{'user_form':user_form,'profile_form':profile_form,'prof_form':prof_form,'registered':registered, 'id':needed_id})
    else:
        return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'prof_form':prof_form,'registered':registered})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                try:
                    if Student.objects.get(StudentID=username) != None:
                        print("bale")
                        the_student = Student.objects.get(StudentID=username)
                        if the_student.Activated:
                            login(request, user)
                        #return HttpResponseRedirect("/signup")

                            return HttpResponse(str(username) + "*Student-Login")
                except:
                    try:
                        if Professor.objects.get(ProfID=username) != None:
                            the_professor = Professor.objects.get(ProfID=username)
                            if the_professor.Activated:
                                login(request, user)
                                return HttpResponse(str(username) + "*Professor-Login")
                    except:
                        return HttpResponse("Invalid login details given")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'index.html', {})


def verification(request, id):
    if request.method == "POST":
        post_dict = dict(request.POST.lists())
        submitted_code = post_dict['verify'][0]
        flag = False
        this = Professor.objects.filter(Q(ProfID=id))

        print(this)
        if len(this) != 0:
            if this[0].VerifyCode == submitted_code:
                Professor.objects.filter(Q(ProfID=id)).update(Activated=True)
                return HttpResponseRedirect(reverse('home'))
        else:
            that = Student.objects.filter(Q(StudentID=id))
            if that[0].VerifyCode == submitted_code:
                Student.objects.filter(Q(StudentID=id)).update(Activated=True)
                return HttpResponseRedirect(reverse('home'))
            
    return render(request, 'VerificationPage.html', {'id':id})

