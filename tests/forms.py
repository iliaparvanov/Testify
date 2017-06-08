from django import forms
from tests.models import Test

class TestForm(forms.ModelForm):
     class Meta:
        model=Test
        fields= ['name']