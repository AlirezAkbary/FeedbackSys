from django import forms

from Student.models import Student
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('degree', 'FirstName', 'LastName', 'profile_pic')
