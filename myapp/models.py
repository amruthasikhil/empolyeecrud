from django.db import models




class Employee(models.Model):
    
    name = models.CharField(max_length=100)
    
    contact = models.CharField(max_length=15, null=True)
    
    salary = models.PositiveIntegerField(null=True)
    
    designation = models.CharField(max_length=100)
    
    department = models.CharField(max_length=100,  null=True)


