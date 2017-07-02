from django.db import models



class Test(models.Model):
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	q_num = models.CharField(max_length=100)
	a_num = models.CharField(max_length=100)

	def __str__(self):
		return self.name + '-' + self.subject

	class Meta:
		ordering = ['pk']

class Questions(models.Model):
	question = models.CharField(max_length=1000)
	name = models.ForeignKey(Test, on_delete = models.CASCADE)
	answer_r = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.name) + '-' + str(self.question)

	class Meta:
		ordering = ['pk']

	
	
	
class Answers(models.Model):
	question = models.ForeignKey(Questions, on_delete = models.CASCADE)
	answer = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.answer)

	class Meta:
		ordering = ['pk']

