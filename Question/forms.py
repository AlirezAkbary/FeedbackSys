from django import forms
from .models import *

class MultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = ('title')

