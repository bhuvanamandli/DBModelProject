from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    sub1 = models.FloatField()
    sub2 = models.FloatField()
    sub3 = models.FloatField()
    total = models.FloatField()
    avg = models.FloatField()

    def __str__(self):
        return 'student Object with sno: ' + str(self.sno)
