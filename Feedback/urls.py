"""Feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.shortcuts import render
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from User.views import signup, user_login, user_logout
from Student.views import student_view
from Professor.views import professor_view,archiveCourseProfessor_view,professorDeleteCourse_view, professorArchiveCourse_view
from . import settings
from Course.views import *
from Question.views import QuestionView
def home_view(request):
    return render(request, "index.html", {})



urlpatterns = [
    path('', user_login, name='home'),
    path('admin/', admin.site.urls),
    path('search/', SearchCourse, name='search_results'),
    path('courseadd/<int:id>/<int:group>', joinCourse, name='join_course'),

    path('signup/', signup, name='signup'),
    path('student/<int:id>', student_view, name='student'),
    path('professor/<int:id>', professor_view, name='professor'),
    path('archiveCourseProfessor/<int:id>', archiveCourseProfessor_view, name='ArchivedCourseProfessor'),
    path('professorDeleteCourse/<int:cid>/<int:gid>', professorDeleteCourse_view, name='professorDeleteCourse'),
    path('professorArchiveCourse/<int:cid>/<int:gid>', professorArchiveCourse_view, name='professorArchiveCourse'),

    path('CourseForm/', AddCourse, name='addcourseform'),
    path('Course/<int:cid>/<int:gid>', courseHome,name="courseHome"),

    path('Course/<int:cid>/<int:gid>/AddMultChoiceQ', AddMultipleChoiceQuestion, name='MultChoiceQ'),

    path('Course/<int:cid>/<int:gid>/Question/<int:qid>', QuestionView),
    url(r'^logout/$', user_logout, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



