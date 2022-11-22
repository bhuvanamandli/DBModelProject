from django.shortcuts import render
from DBModelApp.models import Employee,Company

# Create your views here.

def empdata(req):
    emplist=Employee.objects.all()
    dict1={'emplist':emplist}
    return render(req,'DBModelApp/emp.html',context=dict1)

def compdata(req):
    complist=Company.objects.all()
    dict1={'complist':complist}
    return render(req,'DBModelApp/comp.html',context=dict1)

