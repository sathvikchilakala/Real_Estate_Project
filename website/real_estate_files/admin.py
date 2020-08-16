from django.contrib import admin
# Register your models here.

from .models import EnqDB

# Register your models here.
class EnqDBAdmin(admin.ModelAdmin):
	list_display=['name','mail','mno','message']

admin.site.register(EnqDB,EnqDBAdmin)

from .models import Post

# Register your models here.
class PostDBAdmin(admin.ModelAdmin):
	list_display=['Your_Name_REGISTRATION_REQUIRED','Property_Location','Property_Details','created_date']

admin.site.register(Post,PostDBAdmin)

#fields = ('Your_Name_REGISTRATION_REQUIRED','Property_Location','Property_Details','created_date')
