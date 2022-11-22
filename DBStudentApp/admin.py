from django.contrib import admin
from DBStudentApp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','course','sub1','sub2','sub3','total','avg']

admin.site.register(Student,StudentAdmin)
