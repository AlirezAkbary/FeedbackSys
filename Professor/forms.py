from django import forms

from Professor.models import Professor
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfessorSignUpForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('Degree', 'FirstName', 'LastName', 'profile_pic','Field')
