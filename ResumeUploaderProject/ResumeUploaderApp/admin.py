from django.contrib import admin
from ResumeUploaderApp.models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin','state',
                    'mobile','email','job_city','profile_image','my_file']