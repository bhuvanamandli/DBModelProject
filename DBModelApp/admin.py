from django.contrib import admin
from DBModelApp.models import Employee,Company
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['compid','compname','compemp','compaddr','compshrval']

admin.site.register(Company,CompanyAdmin)