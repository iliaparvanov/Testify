from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .forms import *
from .models import *
from . import *


class QueryExceptionError(Exception):
	def __init__(self):
		super().__init__("No such object")

def index(request):
    return render(request, 'tests/home.html')

def solve(request):
	return render(request, 'tests/solve.html')

def create(request):
	return render(request, 'tests/create.html')

def testChooseMath(request):
	names = [test.name for test in Test.objects.all().filter(subject="Math")]
	br = 1
	results = 1
	wrongs = list()
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br, 'results' : results, 'wrongs' : wrongs})

def testChooseHistory(request):
	names = [test.name for test in Test.objects.all().filter(subject="History")]
	br = 1
	results = 1
	wrongs = list()
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br, 'results' : results, 'wrongs' : wrongs})

def testChooseGeography(request):
	names = [test.name for test in Test.objects.all().filter(subject="Geography")]
	br = 1
	results = 1
	wrongs = list()
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br, 'results' : results, 'wrongs' : wrongs})

def testChooseBiology(request):
	names = [test.name for test in Test.objects.all().filter(subject="Biology")]
	br = 1
	results = 1
	wrongs = list()
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br, 'results' : results, 'wrongs' : wrongs})

def testChooseEnglish(request):
	names = [test.name for test in Test.objects.all().filter(subject="English")]
	br = 1
	results = 1
	wrongs = list()
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br, 'results' : results, 'wrongs' : wrongs})

def addTest(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject', '')
        q_num = request.POST.get('q_num', '')
        a_num = request.POST.get('a_num', '')
        l = list(range(int(a_num)))
        test = Test(name=name, subject=subject, a_num=a_num, q_num=q_num)
        test.save()
        return render(request, 'tests/add.html', {'name' : name, 'q_num' : q_num, 'a_num' : l})

def addQuestions(request):
	if request.method == 'POST':
		test = Test.objects.get(name=request.POST.get('name', ''))
		question = request.POST.get('question', '')
		answer_r = request.POST.get('answer_r', '')
		q_num = request.POST.get("q_num", '')
		q_num = int(q_num)
		a_num = request.POST.get('a_num', '')
		a_num = list(range(int(len(a_num)/3)))

		if int(answer_r) > len(a_num) or int(answer_r) < 1:
			return HttpResponse("Right answer invalid")
		question_o = Questions(name=test, question=question, answer_r=answer_r)
		question_o.save()
		
		
		answers = request.POST.getlist('answer', '')
		for a in answers:
			a = Answers(question=question_o, answer=a)
			a.save()

		if q_num > 1:
			return render(request, 'tests/add.html', {'q_num' : q_num - 1, 'name' : request.POST.get('name', ''), 'a_num' : a_num})
		else:
			return render(request, 'tests/done.html')
		

def getTest(request):
	if request.method == 'POST':

		name = request.POST.get('tests', '')
		test = Test.objects.get(name=name)
		questions = Questions.objects.filter(name=test)
		br = request.POST.get('br', '')
		br = int(br)
		br -= 1
		results = request.POST.get('results', '')
		results = int(results)
		wrongs = request.POST.getlist('wrongs', '')


		
		if br < len(questions):
			answers = Answers.objects.filter(question=questions[br]).order_by('pk')
			
			if br > 0:	
				if str(request.POST.get('answer_right', '')) == str(questions[br - 1].answer_r):
					results += 1
				else:
					wrongs.append(br)
					
			return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : (br + 2), 'answers' : answers, 'results' : results})
		else:

			return render(request, 'tests/doneSolving.html', {'results' : results, "max" : len(questions), 'wrongs' : wrongs})
	