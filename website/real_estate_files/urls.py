from django.conf.urls import url
from .views import Contact,Thanks,StudentInsert,BlogPost,Home,AboutUs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

        url(r'^contact_agent/',Contact,name='contact'),
        url(r'^thanks/',Thanks,name='thankyou'),
        url(r'^post_property/',BlogPost,name='postblog'),
        url(r'^$',Home,name='home'),
        url(r'^aboutus/',AboutUs,name='aboutus'),
		

]
