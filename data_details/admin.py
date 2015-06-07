from django.contrib import admin
from data_details.models import * 
#Register your models here.


class colleges_Admin(admin.ModelAdmin):
    list_display=("college_name","University","state","city")   

class branches_Admin(admin.ModelAdmin):
    list_display=('id','branch_name') 

class subjects_Admin(admin.ModelAdmin):
    list_display=('subject_name','branch') 

class chapters_Admin(admin.ModelAdmin):
    list_display=('chapter_name','subject') 


class notes_details_Admin(admin.ModelAdmin):
    list_display=('college','branch','subject','chapter','pdf_id') 


admin.site.register(colleges,colleges_Admin)

admin.site.register(branches,branches_Admin)

admin.site.register(subjects,subjects_Admin)

admin.site.register(chapters,chapters_Admin)

admin.site.register(notes_details,notes_details_Admin)



