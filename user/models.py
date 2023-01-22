from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50,null=True)
    abbreviation = models.CharField(max_length=2,null=True)

class City(models.Model):
    name = models.CharField(max_length=50,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)

class College(models.Model):
    name = models.CharField(max_length=100,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    
    