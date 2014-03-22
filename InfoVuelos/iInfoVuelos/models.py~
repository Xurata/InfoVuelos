from django.db import models

# Create your models here.

class Airport(models.Model):
	
	#code = models.ForeignKey(max_length=3)
	name = models.TextField(max_length=100)
	#date = models.DateTimeField()
	#amount = models.IntegerField()
	#concept = models.TextField(max_length=100)

class Company (models.Model):

	#code = models.ForeignKey(max_length=2)	
	#airport = models.ForeignKey(Airport)
	name = models.TextField(max_length=100)	
	#date = models.DateTimeField()
	#amount = models.IntegerField()
	#concept = models.TextField(max_length=100)

class Flight (models.Model):

	#code= models.ForeingKey(max_length=5)	
	#company = models.ForeignKey(Company)
	origin = models.TextField(max_length=3)
	destination = models.TextField(max_length=3)
	#date = models.DateField()
	#time = models.TimeField()
	gate = models.TextField(max_length=3)
	

