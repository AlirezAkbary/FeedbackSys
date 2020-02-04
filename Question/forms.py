from django import forms
from .models import *

class MultipleChoiceForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Write a post...',
    #         'type': 'text',
    #         'value' : 'Awli'
    #     }
    # ))
    #
    # class Meta:
    #     model = MultipleChoiceQuestion
    #     fields = ('title',)

    class Meta:
        model = MultipleChoiceQuestion
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'})
        }

