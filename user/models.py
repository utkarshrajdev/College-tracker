from django.db import models

class State(models.Model):
    state = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.state

class City(models.Model):
    city = models.CharField(max_length=50,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.city

class College(models.Model):
    name = models.CharField(max_length=100,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.name
    
    