#!/usr/bin/python3
import random
import datetime

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")

def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z-z!")

# NEW - new view that returns the current date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

def rand(request):
    rint = random.randint(1,10)
    html = "<html>%d</html>" % rint
    return HttpResponse(html)

