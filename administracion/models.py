from django.db import models
from django.contrib import admin
from django.utils import timezone


class Distributor(models.Model):
	Name = models.CharField(max_length=50,unique=True)
	Descripcion = models.CharField(max_length=200)
	Phone = models.CharField(max_length=10,blank=True, null=True)
	Email = models.CharField(max_length=20,blank=True, null=True)
	Address = models.CharField(max_length=50,blank=True, null=True)
	Create = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.Create = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s' % (self.Name, self.Descripcion)

class Reference(models.Model):
	Names = models.CharField(max_length=50,unique=True)
	Last_names = models.CharField(max_length=200)
	Phone = models.CharField(max_length=10,blank=True, null=True)
	DPI = models.CharField(max_length=50,blank=True, null=True)
	Email = models.CharField(max_length=50,blank=True, null=True)
	Distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
	Create = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.Create = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s' % (self.Name, self.Descripcion)

class Brand(models.Model):
	Name = models.CharField(max_length=50,unique=True)
	Descripcion = models.CharField(max_length=200)
	color = models.CharField(max_length=50,blank=True, null=True)
	Create = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.Create = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s' % (self.Name, self.Descripcion)

class AsignBrand(models.Model):
	Distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
	Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	Create = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.Create = timezone.now()
		self.save()
	def __str__(self):
		return '%s %s' % (self.Distributor, self.Brand)
		
class Product(models.Model):
	Code = models.CharField(max_length=70)
	Name = models.CharField(max_length=70)
	Description = models.CharField(max_length=70)
	Brand = models.ForeignKey(AsignBrand, on_delete=models.CASCADE)
	Stock = models.IntegerField(blank=True, null=True)
	Smin = models.IntegerField(blank=True, null=True)
	Smax = models.IntegerField(blank=True, null=True)
	states = (
    	('inactive', 'Inactive'),
	    ('check', 'Check'),
	    ('active', 'Active'),
	    )
	State = models.CharField(
	    max_length=10,
	    choices=states,
	    default='check',
	    )
	Pprice = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
	Sprice = models.DecimalField(max_digits=5, decimal_places=2)
	Note =  models.CharField(max_length=200,blank=True, null=True)
	Create = models.DateTimeField(default=timezone.now,blank=True, null=True)
	def __str__(self):
		return '%s %s %s' % (self.Code,self.Name, self.Descripcion)

class Employee(models.Model):
	Names  =   models.CharField(max_length=70)
	Last_names = models.CharField(max_length=70)
	IdPersonal = models.CharField(max_length=50)
	Phone = models.CharField(max_length=50)
	Address = models.CharField(max_length=200)
	Start_Work = models.DateTimeField(blank=True, null=True)
	states = (
		('inactive', 'Inactive'),
		('active', 'Active'),
		('register', 'register'),
		)
	State = models.CharField(
		max_length=10,
		choices=states,
		default='register',
		)
	Usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE,blank=True, null=True)
	Create = models.DateTimeField(default=timezone.now,blank=True, null=True)
	Note =  models.CharField(max_length=200,blank=True, null=True)
	def __str__(self):
		return '%s %s' % (self.Names, self.Last_names)
