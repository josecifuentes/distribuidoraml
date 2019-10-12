from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Distributor,Reference,Brand,AsignBrand,Product,Employee
import datetime
import calendar
@login_required
def dashboard(request):
	icon = "pe-7s-graph icon-gradient bg-ripe-malin"
	title = "Dashboard"
	text = "Start here, you can check sumary of the sistem if you want you can push the review button."
	pos = "dashboard"
	breacum = []
	brea ={}
	brea["NAME"] = "Dashboard"
	brea["URL"] = "dashboard"
	brea["ICO"] = None
	brea["Active"] = True
	breacum.append(brea)
	brea ={}
	brea["NAME"] = "Home"
	brea["URL"] = "dashboard"
	brea["ICO"] = "pe-7s-home"
	brea["Active"] = None
	breacum.append(brea)
	today = datetime.datetime.now() 
	month = today.month 
	
	return render(request, 'administracion/dashboard.html',{'icon':icon,'title':title,'text':text,'pos':pos,'breacum':breacum})