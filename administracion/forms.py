from django import forms
from django.forms import ModelForm, Textarea
from .models import Distributor,Reference,Brand,AsignBrand,Product,Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('Names', 'Last_names','IdPersonal', 'Phone', 'Address','Email','Birthday', 'Start_Work', 'Usuario', 'Note')
        widgets = {
            'Names': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese los nombres del empleado.'}),
            'Last_names': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese los apellidos del empleado.'}),
            'IdPersonal': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el DPI del empleado.'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el Telefono del empleado.'}),
            'Address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la Direccion del empleado.'}),
            'Email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la Direccion del empleado.'}),
            'Start_Work': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Selecciona la fecha de inicio de trabajo','data-toggle': 'datepicker-year2','autocomplete':'off',}),
            'Birthday': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Selecciona la fecha de nacimiento del empleado','data-toggle': 'datepicker-year','autocomplete':'off',}),
            'Note': Textarea(attrs={'cols': 3, 'rows': 3,'class': 'form-control','placeholder': 'Ingresa una nota para el empleado'}),
        }    
