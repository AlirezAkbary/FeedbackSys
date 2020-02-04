from django import forms
from .models import Course
from Professor.models import Professor
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('CourseID', 'GroupID', 'Name')
    #professor = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Professor ID'}))