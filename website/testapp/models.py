from django.db import models

# Create your models here.
class Employee(models.Model):
	empno=models.IntegerField()
	ename=models.CharField(max_length=30)
	ejob=models.CharField(max_length=30)
	esal=models.FloatField()

	def __str__(self):  
		return self.ename


class Student(models.Model):
	sname=models.CharField(max_length=30)
	course=models.CharField(max_length=30)
	phno=models.IntegerField()
	email=models.EmailField(max_length=80)

	def __str__(self):          
		return self.sname