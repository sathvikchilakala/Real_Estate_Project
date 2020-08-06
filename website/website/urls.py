from django.conf.urls import url,include
from django.contrib import admin
#from blog import views as v1  
#from testapp import views as v2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blogg.urls')),
    url(r'^test/',include('testapp.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),  #<========added
   

]