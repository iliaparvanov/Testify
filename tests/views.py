from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import *
from .models import *
from . import *
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate



class QueryExceptionError(Exception):
	def __init__(self):
		super().__init__("No such object")

def index(request):
    return render(request, 'tests/home.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})


def solve(request):
	test = Test.objects.all()
	l = list()
	l2 = list(range(int(len(test))))

	for i in l2:
		try:
			if test[i].subject not in l:
				l.append(test[i].subject)
		except Exception:
			return HttpResponse("Wrong input")
	return render(request, 'tests/solve.html', {'subjects' : l})

def testChoose(request):
	subjects = request.POST.get('tests', '')
	names = [test.name for test in Test.objects.all().filter(subject=subjects)]
	
	names_and_users = list()
	users = list()
	tests = Test.objects.all().filter(subject=subjects)
	for i in range(len(names)):
		users.append(tests[i].user)
	len1 = len(tests)
	len_list = list(range(len1))
	print(len_list)
	return render(request, 'tests/testChoose.html', {'tests' : tests, 'users' : users, 'len1' : len_list})

def create(request):
	return render(request, 'tests/create.html')

def addTest(request):
	if request.method == 'POST':
		current_user = request.user
		name = request.POST.get('name', '')
		q_num = request.POST.get('q_num', '')
		a_num = request.POST.get('a_num', '')
		subject = request.POST.get('subject', '')
		if Test.objects.filter(name=name):
			alert = "Name already taken!"
			return render(request, 'tests/create.html', {"alert" : alert})

		if Test.objects.filter(subject=subject):
			if 'button_no' in request.POST:
				return render(request, 'tests/create.html', {'name' : name, 'subject' : subject, "q_num" : q_num, "a_num" : a_num})
			elif 'button_yes' in request.POST:
				q_num = request.POST.get('q_num', '')
				a_num = request.POST.get('a_num', '')
				name = request.POST.get('name', '')
				subject = request.POST.get('subject', '')
				l = list(range(int(a_num)))
				if request.user.is_authenticated():
					test = Test(user=current_user, name=name, subject=subject, a_num=a_num, q_num=q_num)
					test.save()
				return render(request, 'tests/add.html', {'name' : name, 'q_num' : q_num, 'a_num' : l})
			else:
				return render(request, 'tests/alert.html', {'name' : name, 'subject' : subject, "q_num" : q_num, "a_num" : a_num})

		
		if not q_num or not a_num or not subject or not name:
			alert = "One or more fields is empty or inccorect"
			return render(request, 'tests/create.html', {"names" : name, "alert" : alert})
		l = list(range(int(a_num)))
		if request.user.is_authenticated():
			test = Test(user=current_user, name=name, subject=subject, a_num=a_num, q_num=q_num)
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
		if not q_num or not a_num:
			alert = "One or more fields are empty"
			return render(request, 'tests/add.html', {'name' : request.POST.get('name', ''), 'q_num' : q_num, 'a_num' : a_num, "alert" : alert})

		if int(answer_r) > int(len(a_num)) or int(answer_r) < 1:
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
			if not request.user.is_authenticated:
				Test.objects.filter(name=request.POST.get('name', '')).delete()
				message = "Your test was created, but was not saved. If you'd like to save a test, please log in"
			else:
				message = "Test successfully created!"
			return render(request, 'tests/done.html', {"message" : message})

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
		wrongs = request.POST.getlist('wrongs')
		print("Wrongs in the beginning: " + str(wrongs))
		br = request.POST.get('br', '')
		br = int(br)
		results = request.POST.get('results', '')
		results = int(results)
		all_wrong = request.POST.get('all_wrong', '')
		all_wrong = int(all_wrong)

#TO DO: WRONGS
		if br < len(questions):
			if br == 0:
				br += 1

			answers = Answers.objects.filter(question=questions[br]).order_by('pk')
			if not str(request.POST.get('answer_right', '')):
				alert = "Field for right answer empty"
				# if br == 1:
				# 	return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : br, 'answers' : answers, 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs, "alert" : alert})
				# else:
				return render(request, 'tests/testSolving.html', {'questions' : questions[br - 1].question, 'tests' : name, 'br' : br, 'answers' : Answers.objects.filter(question=questions[br-1]).order_by('pk'), 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs, "alert" : alert})

			if str(request.POST.get('answer_right', '')) == str(questions[br].answer_r):
					results += 1
					all_wrong = 0

			else:
			#	print("Wrongs when appending: " + str(wrongs))
				wrongs.append(str(br))
				print("Wrongs after append: " + str(wrongs))

			return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : name, 'br' : br + 1, 'answers' : answers, 'results' : results, "all_wrong" : all_wrong, "wrongs" : wrongs})

		else:
			if str(request.POST.get('answer_right', '')) == str(questions[br-1].answer_r):
				results += 1
				all_wrong = 0

			return render(request, 'tests/doneSolving.html', {'results' : results, "max" : len(questions), 'wrongs' : wrongs, "all_wrong" : all_wrong})
