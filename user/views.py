from django.shortcuts import render, redirect
from django.http import HttpResponse
from .scrap import *
from .studyguide import *
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from itertools import chain

def login(request):
  if request.method == 'POST' :
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None :
      auth_login(request, user)
      return redirect('/showcolleges')
    else:
      return HttpResponse("Invalid Credentials OR You are not approved by the admin yet.")
  return render (request, 'login.html')

def showcolleges(request):
    if request.user.is_authenticated :
        u = Employee.objects.get(username=request.user.username)
        states = u.state
        states = states.split(',')
        colleges =[]
        for state in states :
          try:
            temp = College.objects.all().filter(state=state)
            colleges = chain(colleges, temp)
          except:
             pass
        context = {'u': u,'colleges': colleges}
        return render (request,'showcolleges.html',context)
    else :
        return redirect('/login')
    

def register(request):
    if  request.user.is_authenticated and request.user.is_staff :
      if request.method == 'POST' :
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['new_password']
        selectedstates = request.POST.getlist('selectedstates')
        selectedstates = ','.join(selectedstates)
        u = Employee(name=name, username=username, email=email, state=selectedstates)
        u.set_password(password)
        u.save()
        redirect('/register')
      states = State.objects.all()
      context = {'states': states}
      return render (request,'register.html',context)
    else :
      return redirect('/login')

def editcollegedetails(request) :
   if request.method == 'POST' :
    id = request.POST['id']
    c = College.objects.get(id=id)
    c.name = request.POST['name']
    c.city = request.POST['city']
    c.state = request.POST['state']
    c.phone = request.POST['phone']
    c.email = request.POST['email']
    c.website = request.POST['website']
    c.save()
    return redirect('/showcolleges')


def logout(request):
  auth_logout(request)
  return redirect('/login')


def changepassword(request):
  if  request.user.is_authenticated :
    user = Employee.objects.get(email=request.user.email)
    context = {'u': user}
    if request.method == 'POST' :
          password = request.POST['new_password']
          user.set_password(password)
          user.save()
          return redirect('/showcolleges')
    return render (request, 'changepassword.html', context) 
  else :
    return redirect('/login')