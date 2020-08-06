
from django import forms

class ContactForm(forms.Form) :
    contact_name=forms.CharField(max_length=30,required=True)
    contact_email=forms.CharField(required=True)
    phone_number=forms.IntegerField()
    agent_name=forms.CharField(max_length=30,required=True)                                                                                                     
    property_description=forms.CharField(widget=forms.Textarea())

from .models import EnqDB

class EnqDBForm(forms.ModelForm) :
    class Meta :
        model = EnqDB
        fields = ['name','mail','mno','agent','message']# Write only the attributes of the EnqDB class

from .models import Post   #<====added from here

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ('Your_Name_REGISTRATION_REQUIRED','Property_Location','Property_Details','created_date')