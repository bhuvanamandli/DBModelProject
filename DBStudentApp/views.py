from django.shortcuts import render
from DBStudentApp.models import Student
# Create your views here.
def studdata(req):
    studlist=Student.objects.all()
    dict1={'studlist':studlist}
    return render(req,'DBModelApp/stud.html',context=dict1)