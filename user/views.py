from django.shortcuts import render, redirect
from django.http import HttpResponse
from .scrap import *
from .studyguide import *
from .models import College
def scrapcollege(request):
    guide()
    return redirect('/admin')

def scrapstate(request):
    savestate()
    return redirect('/admin')

def scrapcity(request):
    savecity()
    return redirect('/admin')

def showcolleges(request):
    colleges = College.objects.all()
    context = {'colleges': colleges}
    return render (request,'showcolleges.html',context)
