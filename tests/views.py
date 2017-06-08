from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm
from .models import *

def index(request):
    return render(request, 'tests/home.html')

def solve(request):
	return render(request, 'tests/solve.html')

def create(request):
	return render(request, 'tests/create.html')


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        test = Test(name=name)
        test.save()
        return render(request, 'tests/create.html')