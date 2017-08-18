from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


class Test(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	q_num = models.CharField(max_length=100)
	a_num = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['pk']
		permissions = (
			('can_delete', 'Can delete existing tests'),
		)

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

class Mistakes(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.ForeignKey(Test, on_delete = models.CASCADE)
	answer_w = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.answer)

	class Meta:
		ordering = ['pk']
