from django.shortcuts import render, redirect
from django.http import HttpResponse
from .scrap import *
from .studyguide import *
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from itertools import chain
from django.core.paginator import Paginator
import datetime
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from .mail import *
from .sms import *
from django.db.models import OuterRef, Subquery, Value, CharField
from django.contrib import messages
import csv
import json
from django.http import JsonResponse

# // Config
cloudinary.config(
  cloud_name = "dzqr5mmwt",
  api_key = "263454863926658",
  api_secret = "5DfZPkgxd7VM0P1Drp9Sk-vAM9A",
  secure = True
)

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
        query = request.GET.get('p')
        states = u.state
        if request.user.is_staff :
          colleges = College.objects.all()
        else :
          states = states.split(',')
          colleges = College.objects.none()
          for state in states :
            try:
              temp = College.objects.all().filter(state=state)
              colleges = chain(colleges, temp)
            except:
              pass
        
        colleges = colleges.filter(status = "active")
        colleges = list(colleges)
        colleges = College.objects.filter(id__in=[obj.id for obj in colleges])
        object_list = []
        if (query == None):
          object_list = list(colleges)
        else:
              Collegename_list=colleges.filter(name__icontains=query)
              City_list=colleges.filter(city__icontains=query)
              State_list=colleges.filter(state__icontains=query)
              for i in Collegename_list:
                  object_list.append(i)
              for i in City_list:
                  if i not in object_list:
                      object_list.append(i)
              for i in State_list:
                  if i not in object_list:
                      object_list.append(i)
        object_list = list(object_list)
        college_paginator = Paginator(object_list, 30)
        page_num = request.GET.get('page')
        print(page_num)
        page = college_paginator.get_page(page_num)
        surl = request.get_full_path()

    # Append the search query to the URL as a query parameter
        if query:
            surl += '&'
        else :
           surl = '/showcolleges?'
        allfollowup =  Followup.objects.all().order_by('-id')
        context = {'u': u,'page': page,'query': query,'surl': surl,'followup': allfollowup}
        return render (request,'showcolleges.html',context)
    else :
        return redirect('/login')
    

def massmail(request):
    if request.user.is_authenticated :
        if request.method == 'POST' :
          subject = request.POST['subject']
          body = request.POST['body']
          selectedcolleges = request.POST.getlist('selectedcolleges')
          emails = []
          for each in selectedcolleges:
            try :
              c = College.objects.get(id=int(each))
              if ("@" in c.email):
                temp = c.email.split(',')
                for mail in temp :
                  emails.append(mail.strip())
            except:
              pass
          template_mail(subject, emails, 'mailtemplate.html', {'body':body}, '20cs1107@mitsgwl.ac.in')
          messages.success(request, 'Mailed Successfully !!')
        u = Employee.objects.get(username=request.user.username)
        states = u.state
        if request.user.is_staff :
          states = State.objects.all()
          states = [state.state for state in states]
        else :
          states = states.split(',')
        context = {'u': u, 'states':states}
        return render (request,'massmail.html',context)
    else :
        return redirect('/login')


def masssms(request):
    if request.user.is_authenticated :
        if request.method == 'POST' :
          body = request.POST['body']
          selectedcolleges = request.POST.getlist('selectedcolleges')
          numbers = []
          for each in selectedcolleges:
            try :
              c = College.objects.get(id=int(each))
              temp = c.phone.split(',')
              for number in temp :
                numbers.append(number.strip())
            except:
              pass
          sendsms(body,numbers)
          messages.success(request, 'SMS sent Successfully !!')
        u = Employee.objects.get(username=request.user.username)
        states = u.state
        if request.user.is_staff :
          states = State.objects.all()
          states = [state.state for state in states]
        else :
          states = states.split(',')
        context = {'u': u, 'states':states}
        return render (request,'masssms.html',context)
    else :
        return redirect('/login')


def get_colleges_by_state(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_state = data.get('state')

        # Perform the necessary logic to filter colleges based on the selected state
        # Assuming you have a College model with a 'state' field, you can filter the colleges like this:
        colleges = College.objects.all().filter(state=selected_state).filter(status='active')
        # Create a list of dictionaries containing college data to be sent as JSON response
        college_data = [{'id': college.id, 'name': college.name} for college in colleges]
        # Return the college data as a JSON response
        return JsonResponse({'colleges': college_data})
    # If the request method is not POST or an error occurs, return an empty JSON response
    return JsonResponse({'colleges': []})



def inactivecolleges(request):
    if request.user.is_authenticated :
        u = Employee.objects.get(username=request.user.username)
        query = request.GET.get('p')
        states = u.state
        if request.user.is_staff :
          colleges = College.objects.all()
        else :
          states = states.split(',')
          colleges = College.objects.none()
          for state in states :
            try:
              temp = College.objects.all().filter(state=state)
              colleges = chain(colleges, temp)
            except:
              pass
        
        colleges = colleges.filter(status = "inactive")
        colleges = list(colleges)
        colleges = College.objects.filter(id__in=[obj.id for obj in colleges])
        object_list = []
        if (query == None):
          object_list = list(colleges)
        else:
              Collegename_list=colleges.filter(name__icontains=query)
              City_list=colleges.filter(city__icontains=query)
              State_list=colleges.filter(state__icontains=query)
              for i in Collegename_list:
                  object_list.append(i)
              for i in City_list:
                  if i not in object_list:
                      object_list.append(i)
              for i in State_list:
                  if i not in object_list:
                      object_list.append(i)
        object_list = list(object_list)
        college_paginator = Paginator(object_list, 30)
        page_num = request.GET.get('page')
        print(page_num)
        page = college_paginator.get_page(page_num)
        surl = request.get_full_path()

    # Append the search query to the URL as a query parameter
        if query:
            surl += '&'
        else :
           surl = '/inactivecolleges?'
        allfollowup =  Followup.objects.all().order_by('-id')
        context = {'u': u,'page': page,'query': query,'surl': surl,'followup': allfollowup}
        return render (request,'inactivecolleges.html',context)
    else :
        return redirect('/login')

def CollegeSearchView(request):
   if request.user.is_authenticated :
    query = request.GET.get('p')
    object_list = []
    if (query == None):
          object_list = College.objects.all()
    else:
          Collegename_list=College.objects.filter(name__icontains=query)
          City_list=College.objects.filter(city__icontains=query)
          State_list=College.objects.filter(state__icontains=query)
          for i in Collegename_list:
              object_list.append(i)
          for i in City_list:
              if i not in object_list:
                  object_list.append(i)
          for i in State_list:
              if i not in object_list:
                  object_list.append(i)
    
    allfollowup =  Followup.objects.all()
    print(allfollowup)
    context = {
    'colleges': object_list,
    'query': query, 'followup': allfollowup
    }
    return render (request,'showcolleges.html',context) 
   else :
    return redirect('/login')
    

def register(request):
    if  request.user.is_authenticated and request.user.is_staff :
      u = Employee.objects.get(username=request.user.username)
      if request.method == 'POST' :
        name = request.POST['name']
        fathername = request.POST['fathername']
        mobile = request.POST['mobile']
        gender = request.POST['gender']
        aadhar = request.POST['aadhar']
        username = request.POST['username']
        email = request.POST['email']
        role = request.POST['email']
        password = username + "@123"
        selectedstates = request.POST.getlist('selectedstates')
        selectedstates = ','.join(selectedstates)
        lst = Employee.objects.all().filter(email=email).exists()
        lst2 = Employee.objects.all().filter(username=username).exists()
        if lst :
           messages.warning(request, 'User with same email already exists !!')
        elif lst2 :
           messages.warning(request, 'User with same username already exists !!')
        else :
          n = Employee(name=name, username=username, fathername = fathername, mobile = mobile,
                      gender = gender, aadhar = aadhar, email=email, state=selectedstates)
          n.set_password(password)
          n.save()
          if ( role == "Staff") :
             n.is_staff = True
             n.save()
          messages.success(request, 'User Successfully Registered !!')
          try:
            template_mail('College Tracker - Successfully Registered', [email], 'registermail.html', {'user': n, 'password':password}, 
            '20cs1107@mitsgwl.ac.in')
          except :
            pass
          redirect('/register')
      states = State.objects.all()
      context = {'u': u,'states': states}
      return render (request,'register.html',context)
    else :
      return redirect('/login')
    
def savefollowup(request):
    if  request.user.is_authenticated :
      if request.method == 'POST' :
        collegeid = request.POST['collegeid']
        message = request.POST['message']
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        ins = Followup(collegeid=collegeid, message=message, date=current_date, time=current_time, 
        employee = request.user.username)
        ins.save()
        return redirect('/showcolleges')
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
    c.status = request.POST['status']
    category = request.POST['category']
    if category == "":
        c.category = None
    else:
        c.category = category
    courses = request.POST.getlist('courses[]')
    if not courses:
        courses = None
    c.courses = courses
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
  



def editprofile(request):
    if  request.user.is_authenticated :
      u = Employee.objects.get(username=request.user.username)
      if request.method == 'POST' :
        u.name = request.POST['name']
        u.fathername = request.POST['fathername']
        u.mobile = request.POST['mobile']
        u.gender = request.POST['gender']
        u.aadhar = request.POST['aadhar']
        u.username = request.POST['username']
        u.email = request.POST['email']
        try :
          profileimage = request.FILES['profileimage']
          cloudinaryname = u.username+str(u.id)
          upload(profileimage, public_id=cloudinaryname)

          # // Transform
          url, options = cloudinary_url(cloudinaryname, width=100, height=100, crop="fill")
          u.imageurl = url
        except :
           pass
        u.save()
        messages.success(request, 'Profile Successfully Updated !!')
        redirect('/showcolleges')
      context = {'u': u,'user':u,}
      return render (request,'editprofile.html',context)
    else :
      return redirect('/login')


def showfollowup(request):
    if  request.user.is_authenticated :
        u = Employee.objects.get(username=request.user.username)
        query = request.GET.get('p')
        colleges = College.objects.all()
        followups = Followup.objects.all()
        #college_lookup = {college.id: college.name for college in colleges}
        college_lookup = College.objects.filter(id=OuterRef('collegeid')).values('name')[:1]

# Get the queryset of all followups with college names
        followups = Followup.objects.annotate(collegename=Subquery(college_lookup, output_field=CharField()))
        followups = followups.order_by('-id')
        #followups = Followup.objects.annotate(collegename=Subquery(College.objects.filter(collegeid=F('collegeid')).values('collegename')[:1]))
        #followups = followups.annotate(collegename=F('collegeid__collegename'))
        if request.user.is_staff :
          followups = followups
        else :
          followups = followups.filter(employee=request.user.username)
        object_list = []
        if (query == None):
          object_list = list(followups)
        else:
              Collegename_list=followups.filter(collegename__icontains=query)
              Employee_list=followups.filter(employee__icontains=query)
              for i in Collegename_list:
                  object_list.append(i)
              for i in Employee_list:
                  if i not in object_list:
                      object_list.append(i)
        object_list = list(object_list)
        college_paginator = Paginator(object_list, 30)
        page_num = request.GET.get('page')
        print(page_num)
        page = college_paginator.get_page(page_num)
        surl = request.get_full_path()

    # Append the search query to the URL as a query parameter
        if query:
            surl += '&'
        else :
           surl = '/showfollowup?'
        allfollowup =  Followup.objects.all()
        context = {'u': u,'page': page,'query': query,'surl': surl,'followup': allfollowup, 'colleges': colleges}
        return render (request,'showfollowup.html',context)
    else :
        return redirect('/login')


def allemployee(request):
    if  request.user.is_authenticated and request.user.is_staff :
        if request.method == 'POST' :
          e = Employee.objects.get(username=request.POST['username'])
          e.name = request.POST['name']
          e.mobile = request.POST['mobile']
          e.fathername = request.POST['fathername']
          e.aadhar = request.POST['aadhar']
          role = request.POST['aadhar']
          selectedstates = request.POST.getlist('selectedstates')
          selectedstates = ','.join(selectedstates)
          e.state = selectedstates
          if (role == "Staff"):
             e.is_staff = True
          else :
             e.is_staff = False
          e.save()
        u = Employee.objects.get(username=request.user.username)
        query = request.GET.get('p')
        employees = Employee.objects.all()
        object_list = []
        states = State.objects.all()
        try: 
          for employee in employees:
            employee.state = employee.state.split(',')
        except:
           pass
        if (query == None):
          object_list = list(employees)
        else:
              Name_list=employees.filter(name__icontains=query)
              Username_list=employees.filter(username__icontains=query)
              Email_list=employees.filter(email__icontains=query)
              State_list=employees.filter(state__icontains=query)
              for i in Name_list:
                  object_list.append(i)
              for i in Username_list:
                  if i not in object_list:
                      object_list.append(i)
              for i in Email_list:
                  if i not in object_list:
                      object_list.append(i)
              for i in State_list:
                  if i not in object_list:
                      object_list.append(i)
        object_list = list(object_list)
        college_paginator = Paginator(object_list, 30)
        page_num = request.GET.get('page')
        print(page_num)
        page = college_paginator.get_page(page_num)
        surl = request.get_full_path()

    # Append the search query to the URL as a query parameter
        if query:
            surl += '&'
        else :
           surl = '/allemployee?'
        allfollowup =  Followup.objects.all()
        context = {'u': u,'page': page,'query': query,'surl': surl, 'states':states}
        return render (request,'allemployee.html',context)
    else :
        return redirect('/login')
    





def addcollege(request):
    if  request.user.is_authenticated :
      u = Employee.objects.get(username=request.user.username)
      if u.is_staff :
         states = State.objects.all()
         states = [state.state for state in states]
      else :
        states = u.state.split(',')
      if request.method == 'POST' :
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']
        c = College(name = name, city = city, state = state, phone = phone, email = email, website = website)
        c.save()
        messages.success(request, 'College Successfully Registered !!')
        redirect('/showcolleges')
      context = {'u': u,'user':u, 'states': states}
      return render (request,'addcollege.html',context)
    else :
      return redirect('/login')
    



