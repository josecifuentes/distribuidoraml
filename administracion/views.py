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
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeForm
from django.db import IntegrityError, transaction
import datetime
import calendar
@login_required
def dashboard(request):
	icon = "pe-7s-graph icon-gradient bg-ripe-malin"
	title = "Principal"
	text = "Comience aquí, puede consultar el resumen del sistema si lo desea, puede presionar el botón de revisión."
	pos = "dashboard"
	per = True
	breacum = []
	brea ={}
	brea["NAME"] = "Inicio"
	brea["URL"] = "dashboard"
	brea["ICO"] = "pe-7s-home"
	brea["Active"] = None
	breacum.append(brea)
	brea ={}
	brea["NAME"] = "Principal"
	brea["URL"] = "dashboard"
	brea["ICO"] = None
	brea["Active"] = True
	breacum.append(brea)
	
	today = datetime.datetime.now() 
	month = today.month 
	
	return render(request, 'administracion/dashboard.html',{'icon':icon,'title':title,'text':text,'pos':pos,'breacum':breacum,'per':per})
@login_required
def newemployee(request):
	icon = "pe-7s-user icon-gradient bg-ripe-malin"
	title = "Nuevo Empleado"
	text = "Formulario para agregar empleados y agregar el usuario para el acceso porterior al sistema."
	pos = "newemployee"
	per = None
	breacum = []
	brea ={}
	brea["NAME"] = "Empleados"
	brea["URL"] = "listemployee"
	brea["ICO"] = "pe-7s-users"
	brea["Active"] = None
	breacum.append(brea)
	brea ={}
	brea["NAME"] = "Nuevo Empleado"
	brea["URL"] = "newemployee"
	brea["ICO"] = None
	brea["Active"] = True
	breacum.append(brea)
	errores=None
	mensajes=None
	button="Nuevo Empleado"
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		print(request.POST['User'])
		if request.POST['User'] != "":
			if request.POST['Start_Work'] != "":
				try:
					User.objects.get(username=request.POST['User'])
				except User.DoesNotExist:
					if form.is_valid():
						try:
							with transaction.atomic():
								post = form.save(commit=False)
								post.State = "Registro"
								usuario = User.objects.create_user(username=request.POST['User'],password="Embutidos123")
								g = Group.objects.get(name=request.POST['UserType'])
								g.user_set.add(User.objects.get(username=usuario))
								post.Usuario=User.objects.get(username=usuario)
								post.save()
								mensajes="Se ha creado el usuario "+ request.POST['User'] + " con exito!"
								form = EmployeeForm()
						except IntegrityError:
							handle_exception()
							errores="No se ha podido guardar revise los campos para continuar..."
					else:
						errores="No se ha podido guardar revise los campos para continuar..."
			else:
				errores="No se puede ingresar el empleado sin una fecha de inicio laboral..."
		else:
			errores="No se puede ingresar el empleado sin un usuario..."
	else:
		mensajes=None
		form = EmployeeForm()
	return render(request, 'administracion/newemployee.html', {'icon':icon,'title':title,'pos':pos,'text':text,'breacum':breacum,'button': button,'form': form,'mensajes': mensajes,'errores': errores,'per':per})
@login_required
def listemployee(request):
	icon = "pe-7s-users"
	title = "Listado de empleados"
	text = "Listado de empleados pede actualizar datos y/o eliminar empleados."
	pos = "employee"
	per = None
	breacum = []
	brea ={}
	brea["NAME"] = "Empleados"
	brea["URL"] = "listemployee"
	brea["ICO"] = "pe-7s-users"
	brea["Active"] = None
	breacum.append(brea)
	employees = Employee.objects.all()
	try:
		mensajes = request.session['mensajes']
		del request.session['mensajes']
	except Exception as e:
		mensajes=None
	try:
		errores = request.session['errores']
		del request.session['errores']
	except Exception as e:
		errores=None
	return render(request, 'administracion/employee.html', {'icon':icon,'title':title,'pos':pos,'text':text,'breacum':breacum,'employees': employees,'mensajes': mensajes,'errores': errores,'per':per})
