from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib import messages

from time import gmtime, strftime
from datetime import datetime
import random
import bcrypt
from django.contrib.auth.decorators import login_required
from . models import *


def index(request):

   return render(request, "login_app/landing_page.html")

def login_page(request):

   return render(request, "login_app/login_page.html")


def show(request):

   return render(request, "login_app/patient_grid.html")

def register(request):
   if request.method=="POST":

      request.session['first_name'] = request.POST.get('first_name')
      request.session['last_name'] = request.POST.get('last_name')
      request.session['email'] = request.POST.get('email')
     

      errors = User.objects.basic_validator(request.POST)
      if len(errors) > 0:
         for key, value in errors.items():
            # print(key, value + '\n')
            messages.add_message(request, messages.INFO,  value)
         return redirect('/login_page')
      
   password=request.POST['password']
   mypassstring = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
       
   try:
      checkemail = User.objects.get(email = request.POST['email'])
           
      if request.POST['email'] == checkemail.email:
         messages.add_message(request, messages.INFO, "YOU ARE ALREADY REGISTERED!")
         return redirect('/login_page')
   except User.DoesNotExist:       
      user1=User.objects.create(
         first_name=request.POST['first_name'],\
         last_name=request.POST['last_name'], \
         email=request.POST['email'],\
         password = mypassstring, 
         )
      
      request.session['id']=user1.id
      

      return redirect("/dash/show")

def login(request):
   if request.method=="POST":
    
      # checking if password or email fields are empty
      if not request.POST['email'] or not request.POST['password']:
         messages.add_message(request, messages.INFO, "Email and Password are required!")
         return redirect ("/login_page")
      

      password=request.POST['password']
      try:
         getinfo = User.objects.get(email = request.POST['email'])
      except:
         messages.add_message(request, messages.INFO, "Email or Password does not match!")
         return redirect ("/login_page")
      
      request.session['id'] = getinfo.id
      print(getinfo.email, getinfo.password)

      val = bcrypt.checkpw(password.encode('utf8'), getinfo.password.encode('utf8'))
      print(val)

      if val:
         request.session['first_name'] = getinfo.first_name
         return redirect("/dash/show")
      else:
         messages.add_message(request, messages.INFO, "Email or Password does not match!")
         return redirect ("/login_page")
  


def logout(request):
    request.session.clear() 
    return redirect ("/")



