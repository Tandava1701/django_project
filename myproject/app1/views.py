from urllib import request

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import *

def home(request):
  l=loader.get_template('home.html')
  return HttpResponse(l.render())

def home2(request):
  t=loader.get_template('interier.html')
  return HttpResponse(t.render())

def signup(request):
  t=loader.get_template('sign up.html')
  return HttpResponse(t.render())

@csrf_exempt
def home3(request):
  if request.method=="POST":
    username=request.POST["customer_name"]
    email=request.POST["email_address"]
    password=request.POST["comments"]
    z=User.objects.create_user(username=username,email=email,password=password)
    z.save()
    return render(request,'hai.html')

def login(request):
  t=loader.get_template('sign in.html')
  return HttpResponse(t.render())

@csrf_exempt
def login1(request):
  if request.method=="POST":
    uname=request.POST['username']
    passwrd=request.POST['password']
    valid=auth.authenticate(username=uname,password=passwrd)
    if valid is not None:
      auth.login(request,valid)
      return render(request,'hai.html')
    else:
      return HttpResponse("INVALID")

@csrf_exempt
def logout(request):
  auth.logout(request)
  return redirect('/')


def service(request):
  t=loader.get_template('service.html')
  return HttpResponse(t.render())


def order(request):
  t=loader.get_template('order.html')
  return HttpResponse(t.render())


def aboutus(request):
  t=loader.get_template('aboutus.html')
  return HttpResponse(t.render())


def order1(request):
  t=loader.get_template('order1.html')
  return HttpResponse(t.render())
