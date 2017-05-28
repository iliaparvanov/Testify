from django import forms

class HomeForm(form.Form):
	post = forms.ChartField()