from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

def Home(request):
	return HttpResponse('<body bgcolor="yellow"> Welcome to test app page home page<br></body>')

def Employees(request):
	context={'empdb':Employee.objects.all()}
	return render(request,'emp.html',context)

def testappTest(request):
    context={}
    return render(request,'testapp/test.html',context)
