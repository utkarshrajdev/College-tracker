from django.db import models
from django.contrib.auth.models import AbstractUser

class State(models.Model):
    state = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.state

                
class Employee(AbstractUser) :
    name = models.CharField(max_length=32 ,null = True)
    state = models.CharField(max_length=1000,null=True)
    mobile = models.CharField(max_length=32 ,null = True)
    fathername = models.CharField(max_length=32 ,null = True)
    gender = models.CharField(max_length=32 ,null = True)
    aadhar = models.CharField(max_length=32 ,null = True)
    
    def __str__(self) :
        return self.username


class City(models.Model):
    city = models.CharField(max_length=50,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.city
    



class College(models.Model):
    CATEGORY_CHOICES = (
        ('IIT', 'IIT'),
        ('NIT', 'NIT'),
        ('Other', 'Other')
    )
    COURSE_CHOICES = (
        ('BTech', 'BTech'),
        ('MTech', 'MTech'),
        ('MS', 'MS'),
        ('MBA', 'MBA')
    )
    name = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    website = models.URLField(max_length=100,null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=True)
    courses = models.CharField(max_length=10, choices=COURSE_CHOICES,null=True)
    

    def __str__(self) :
        return self.name
    


class Followup(models.Model):
    collegeid = models.IntegerField(null=True)
    date = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100,null=True)
    message = models.CharField(max_length=512,null=True)
    
    