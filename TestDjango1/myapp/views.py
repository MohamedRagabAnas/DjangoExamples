# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context

def hello(request):
	today = datetime.datetime.now().date()
	daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def BSTemplate(request):
	return render(request, "index.html", {})

def hello_template(request):
	name="Mohamed"
	t= get_template("hello.html")
	html=t.render( {"name":name})
	return HttpResponse(html)

def hello_template_simple(request):
	name="Mohamed"
	return render_to_response( "hello.html", {"name":name})
	


   
# Create your views here.
