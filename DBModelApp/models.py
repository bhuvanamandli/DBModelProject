from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField();
    ename = models.CharField(max_length=30);
    esal = models.FloatField();
    eaddr = models.CharField(max_length=30);

    def __str__(self):
        return 'Employee Object with eno: ' + str(self.eno);

class Company(models.Model):
    compid=models.IntegerField()
    compname=models.CharField(max_length=30) #single-line-txt
    compemp=models.IntegerField()
    compaddr=models.TextField() #multi-line-txt
    compshrval=models.FloatField()

    def __str__(self):
        return 'Company details'+str(self.compid)


