from django.http import HttpResponse

def AboutUs(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my AboutUs Page</h1></center><br></body>')
	
def Contact(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my contact page</h1></center><br></body>')

def Product(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my Product page</h1></center><br></body>')

def Hello(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Hello!!! Welcome to my blog page</h1></center><br></body>')

from django.http import HttpResponse
from django.shortcuts import render

def HelloTemplate(request):
	context={}
	return render(request,'hello.html',context)

def ProductStatic(request):
    context={}
    return render(request,'prod.html',context)

def ProductDynamicOneRecord(request):
    context={'pid':1001,'pname':'Django Framework','price':450,'author':'Milton'}
    return render(request,'prodonedy.html',context)

def Products(request):
    context={'proddb':[
    {'pid':101,'pname':'Dive into python 3','price':450,'author':'Milton'},
    {'pid':102,'pname':'Python algorithms','price':550,'author':'Charles'},
    {'pid':103,'pname':'Networking python','price':650,'author':'Miller'},
    {'pid':104,'pname':'Advanced python','price':350,'author':'Robert'},
    {'pid':105,'pname':'Python for automation','price':367,'author':'Smith'}
                      ]}
    return render(request,'prodsmultiple.html',context)

from .models import Post   
def BlogData(request): 
    context={'blogdb':Post.objects.all()}
    return render(request,'blog_data.html',context)

def bloggTest(request):
    context={}
    return render(request,'blogg/test.html',context)

def Thanks(request): 
    #return HttpResponse("Thank you and Have a great day!!!,I will inform you soon")
    return render(request,'blogg/thankyou.html',{})

from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage

from .forms import ContactForm

def Contact(request): 
    
    form_class = ContactForm 
    context = {'form':form_class}
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            phno=form.cleaned_data['phno']
            content = form.cleaned_data['text']
            subject = "A new contact or lead - {}".format(contact_name)
            email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + str(phno) +'\n'+content , to=['sathvik.chilakala@gmail.com'])
            email.send()
            return HttpResponseRedirect('/blog/thanks/') #project-url/app-url       
    return render(request,'blogg/blog_contact.html',context)

from .forms import EnqDBForm
from .models import EnqDB

def  StudentInsert(request) :   
    

    # POST
    if request.method == 'POST':
        form = EnqDBForm(request.POST)
        #print(form.is_valid())
        # when your form is valid
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            mno = form.cleaned_data['mno']
            message = form.cleaned_data['message']
            EnqDB.objects.create(name=name,mail=mail,mno=mno,message=message) #To create the                                                                                     #table in the                                                                                     #database
            return HttpResponseRedirect('/blog/thanks/')
        # when my form is not valid
        else:
            context = {'form':form}
            return render(request,'blogg/contactform.html',context)
    # GET
    else:
        form = EnqDBForm
        context={'form':form}
        return render(request,'blogg/contactform.html',context)

from .forms import PostForm   #<==========Added from here
from .models import Post

def BlogPost(request):
    print(request.method)#To see which method has been called
    # GET REQUEST
    form_class = PostForm  # class not a instance
    context = {'form':form_class}
    
    # POST REQUEST
    if request.method == 'POST':
        form = PostForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            Your_Name_REGISTRATION_REQUIRED = form.cleaned_data['Your_Name_REGISTRATION_REQUIRED']
            Property_Location = form.cleaned_data['Property_Location']
            Property_Details=form.cleaned_data['Property_Details']
            created_date = form.cleaned_data['created_date']
            Post.objects.create(Your_Name_REGISTRATION_REQUIRED=Your_Name_REGISTRATION_REQUIRED,Property_Location=Property_Location,Property_Details=Property_Details,created_date=created_date)
            return HttpResponseRedirect('/blog/thanks/')            
    return render(request,'blogg/post_blog.html',context)

def Home(request):
    context={}
    return render(request,'home.html',context)

def AboutUs(request):
    context={}
    return render(request,'blogg/about_us.html',context)

def   Home(request) :
    context={'blogdb':Post.objects.all()}
    return render(request,'home.html',context)



