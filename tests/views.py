from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .forms import *
from .models import *
from . import *

class InvalidNodeError(Exception):
	def __init__(self):
		super().__init__('Attempting to enqueue a None value to the queue is forbidden.')

class Queue:
	def __init__(self):
		self.head = self.tail = None
		self.size = 0
		
	class Node:
		def __init__(self, value):
			self.value = value
			self.prev = None
			
	def enqueue(self, value):

		new_node = Queue.Node(value)
		
		if self.is_empty():
			self.head = self.tail = new_node
		else:
			self.tail.prev = new_node
			self.tail = new_node
			
		self.size += 1
		
	def dequeue(self):
		dequeued_value = None
		
		if self.is_empty():
			dequeued_value = None
		elif self.size == 1:
			dequeued_value = self.head.value
			self.head = self.head.prev
			self.tail = None
		else:
			dequeued_value = self.head.value
			self.head = self.head.prev
			
			
		self.size = (self.size - 1) if self.size > 0 else 0
		
		return dequeued_value
		
	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.head.value
		
	def clear(self):
		self.head = self.tail = None
		self.size = 0
		
	def __iter__(self):
		return Queue.Iterator(self)
		
	class Iterator:
		def __init__(self, queue):
			self.queue = queue
			
		def __next__(self):
			dequeued_value = self.queue.dequeue()
			if dequeued_value == None:
				raise StopIteration
			else:
				return dequeued_value
		
	def __len__(self):
		return self.size
		
	def is_empty(self):
		return self.head == None and self.tail == None
			
def print_queue(q):
	current = q.head
	if current == None:
		return
		
	while current != None:
		print(current.value)
		current = current.prev

def print_info(msg, q):
	print(msg)
	print('queue size: {}'.format(len(q)))
	print_queue(q)
	print()

def dequeue_q(q):
	for value in q:
		print('dequeued: {}'.format(value))




class QueryExceptionError(Exception):
	def __init__(self):
		super().__init__("No such object")

def index(request):
    return render(request, 'tests/home.html')

def solve(request):
	return render(request, 'tests/solve.html')

def create(request):
	return render(request, 'tests/create.html')

def testChoose(request):
	names = [test.name for test in Test.objects.all().filter(subject="Scripting")]
	br = 1
	return render(request, 'tests/testChoose.html', {'names' : names, 'br' : br})


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
	tail = Queue()
	if request.method == 'POST':

		answer = request.POST.get('tests', '')
		test = Test.objects.get(name=answer)
		questions = Questions.objects.filter(name=test)
		br = request.POST.get('br', '')
		br = int(br)
		br -= 1


		if br < len(questions):

			return render(request, 'tests/testSolving.html', {'questions' : questions[br].question, 'tests' : answer, 'br' : (br + 2)})
		else:
			return HttpResponse("Done")
	