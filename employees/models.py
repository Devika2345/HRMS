from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    attendance = models.IntegerField()  

    def _str_(self):
        return self.name
