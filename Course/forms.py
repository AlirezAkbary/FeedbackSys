from django import forms
from .models import Course
from Professor.models import Professor
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('CourseID', 'GroupID', 'Name')
        widgets = {
            'CourseID': forms.TextInput(attrs={'class': 'form-control'}),
            'GroupID': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'})
        }



    #professor = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Professor ID'}))