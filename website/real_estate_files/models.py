from django.utils import timezone
from django.db import models

class Post(models.Model):
	Your_Name_REGISTRATION_REQUIRED=models.ForeignKey('auth.user')
	Property_Location=models.CharField(max_length=30)
	Property_Details=models.TextField() 
	created_date=models.DateTimeField(default=timezone.now())
	published_date=models.DateField(blank=True,null=True) 
	
	def __str__(self):
		return self.Property_Location

from django.db import models
from django.utils import timezone
from django import forms
class EnqDB(models.Model) :
	contact_name=models.CharField(max_length=30)
	contact_email=models.CharField(max_length=30)
	phone_number=models.IntegerField()
	agent_name=models.CharField(max_length=30)
	property_description=models.CharField(max_length=60)
	
	def __str__(self):
		return self.contact_email