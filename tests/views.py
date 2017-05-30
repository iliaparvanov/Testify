from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'tests/home.html')

def solve(request):
	return render(request, 'tests/solve.html')

def create(request):
	return render(request, 'tests/create.html')

def add(request):
	name1 = request.Get.get("name")
#	subject = request.Get.get("subject")
#	q_num = request.Get.get("q_num")
#	a_num= request.Get.get("a_num")

	test = Test(name = name1)
	test.save()

def post_subject(request):
	subject = request.Get.get("subject")

def post_test(request):
	pk = request.Get.get("pk")
	tests = Test.objects.all()

	return JsonResponse({"name" : tests[pk].name, "q_num" : tests[pk].q_num, "a_num" : tests[pk].a_num})


