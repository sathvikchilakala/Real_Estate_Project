from django.contrib import admin

from .models import EnqDB

class EnqDBAdmin(admin.ModelAdmin):
	list_display=['contact_name','contact_email','phone_number','agent_name','property_description']

admin.site.register(EnqDB,EnqDBAdmin)

from .models import Post

class PostDBAdmin(admin.ModelAdmin):
	list_display=['Your_Name_REGISTRATION_REQUIRED','Property_Location','Property_Details','created_date']

admin.site.register(Post,PostDBAdmin)


