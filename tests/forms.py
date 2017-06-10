from django import forms
from tests.models import *

class TestForm(forms.ModelForm):
     class Meta:
        model=Test
        fields= ['name', 'subject', 'q_num', 'a_num']

class QuestionForm(forms.ModelForm):
     class Meta:
        model=Questions
        fields= ['name', 'question']