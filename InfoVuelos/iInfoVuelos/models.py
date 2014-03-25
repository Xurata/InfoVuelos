from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Airport(models.Model):
	name = models.TextField(max_length=100)
	code = models.TextField(max_length=3)
	city = models.TextField(max_length=100)
	def __unicode__(self):
		return self.name

class Company (models.Model):
	airport = models.ManyToManyField(Airport)
	name = models.TextField(max_length=100)	
	code = models.TextField(max_length=2)
	user = models.ForeignKey(User) # Preguntar a francesc !!!!
	def __unicode__(self):
		return self.name+" - "+self.code

class Flight (models.Model):
	code = models.TextField(max_length=5)
	origin = models.TextField(max_length=3)
	destination = models.TextField(max_length=3)
	gate = models.TextField(max_length=3)
	company = models.ForeignKey(Company)
