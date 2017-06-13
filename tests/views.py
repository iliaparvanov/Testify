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
	return render(request, 'tests/testChoose.html', {'names' : names})

def testChooseHistory(request):
	names = [test.name for test in Test.objects.all().filter(subject="History")]
	return render(request, 'tests/testChoose.html', {'names' : names})

def testChooseGeography(request):
	names = [test.name for test in Test.objects.all().filter(subject="Geography")]
	return render(request, 'tests/testChoose.html', {'names' : names})

def testChooseBiology(request):
	names = [test.name for test in Test.objects.all().filter(subject="Biology")]
	return render(request, 'tests/testChoose.html', {'names' : names})

def testChooseEnglish(request):
	names = [test.name for test in Test.objects.all().filter(subject="English")]
	return render(request, 'tests/testChoose.html', {'names' : names})

def addTest(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if Test.objects.filter(name=name):
        	alert = "Name already taken!"
        	return render(request, 'tests/create.html', {"alert" : alert})
        subject = request.POST.get('subject', '')
        if not subject:
        	alert = "Field for subject empty. Please specify your subject"
        	return render(request, 'tests/create.html', {"alert" : alert})
        q_num = request.POST.get('q_num', '')

        if not q_num:
        	alert = "Field for questions number empty. Please specify the number of questions"
        	return render(request, 'tests/create.html', {"alert" : alert})
        a_num = request.POST.get('a_num', '')
        if not a_num:
        	alert = "Field for answers number empty. Please specify the number of answers"
        	return render(request, 'tests/create.html', {"alert" : alert})

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
		if not q_num or a_num:
			alert = "One or more fields are empty"
			return render(request, 'tests/add.html', {'name' : request.POST.get('name', ''), 'q_num' : q_num, 'a_num' : a_num, "alert" : alert})

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
		br = 0
		results = 0
		all_wrong = 1
		wrongs = list()
		answers = Answers.objects.filter(question=questions[br]).order_by('pk')
			
		
		return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : br, 'answers' : answers, 'wrongs' : wrongs, 'results' : results, 'all_wrong' : all_wrong})

			


def solveTest(request):
	if request.method == 'POST':
		name = request.POST.get('tests', '')
		test = Test.objects.get(name=name)
		questions = Questions.objects.filter(name=test)
		wrongs = request.POST.getlist('wrongs', '')
		br = request.POST.get('br', '')
		br = int(br)
		results = request.POST.get('results', '')
		results = int(results)
		all_wrong = request.POST.get('all_wrong', '')
		all_wrong = int(all_wrong)
		
		

		if br < len(questions):
			answers = Answers.objects.filter(question=questions[br]).order_by('pk')
			if not str(request.POST.get('answer_right', '')):
				alert = "Field for right answer empty"
				if br == 0:
					return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : br, 'answers' : answers, 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs, "alert" : alert})
				else:
					return render(request, 'tests/testSolving.html', {'questions' : questions[br - 1].question, 'tests' : name, 'br' : br, 'answers' : answers, 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs, "alert" : alert})
			if str(request.POST.get('answer_right', '')) == str(questions[br].answer_r):
					results += 1
					all_wrong = 0

			else:
				wrongs.append(br)


			if br == 0:
				br += 1
			
			return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : br + 1, 'answers' : answers, 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs})
			
		else:

			return render(request, 'tests/doneSolving.html', {'results' : results, "max" : len(questions), 'wrongs' : wrongs, "all_wrong" : all_wrong})
		