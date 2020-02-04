from django.shortcuts import render
from Student.forms import UserSignUpForm, StudentSignUpForm
from Professor.forms import ProfessorSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Professor.models import Professor
from Student.models import Student
import copy
import json
# Create your views here.


def signup(request):

    registered = False
    a = copy.deepcopy(str(request.body))
    #print(a)
    if request.method == 'POST':
        print(request.method, "akbar")

        if a.find("\x46\x69\x65\x6c\x64") != -1 or a.find("Field") != -1:
            user_form = UserSignUpForm(data=request.POST)
            prof_form = ProfessorSignUpForm(data=request.POST)
            profile_form = StudentSignUpForm()
            if user_form.is_valid() and prof_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = prof_form.save(commit=False)
                profile.user = user
                profile.ProfID = user.username
                if 'profile_pic' in request.FILES:
                    #print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
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
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.StudentID = user.username
                if 'profile_pic' in request.FILES:
                    #print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
            else:
                pass
                #print(user_form.errors, profile_form.errors)

    else:
        user_form = UserSignUpForm()
        profile_form = StudentSignUpForm()
        prof_form = ProfessorSignUpForm()


    print("AWLIIIII", registered)
    #return HttpResponse("user logged in")
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
                        login(request, user)
                        #return HttpResponseRedirect("/signup")

                        return HttpResponse(str(username) + "*Student-Login")
                except:
                    try:
                        if Professor.objects.get(ProfID=username) != None:
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