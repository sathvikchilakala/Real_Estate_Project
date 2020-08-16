from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^real_estate/',include('real_estate_files.urls')),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
   
]