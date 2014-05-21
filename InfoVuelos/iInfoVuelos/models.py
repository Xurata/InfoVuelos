from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Airport(models.Model):
	name = models.TextField(max_length=100)
	code = models.TextField(max_length=3)
	city = models.TextField(max_length=100)
	def __unicode__(self):
		return self.name+" - "+self.code+" - "+self.city

class Company (models.Model):
	airport = models.ManyToManyField(Airport)
	name = models.TextField(max_length=100)	
	code = models.TextField(max_length=2)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.name+" - "+self.code

	def get_absolute_url(self):
		return reverse('company_detail', kwargs = {'pk' : self.pk})

class Flight (models.Model):
	code = models.TextField(max_length=5)
	origin = models.TextField(max_length=3)
	destination = models.TextField(max_length=3)
	gate = models.TextField(max_length=3)
	#company = models.OneToOneField(Company)
	#airport = models.ManyToOneField(Airport)
	user = models.ForeignKey(User)
	#airport = models.ForeignKey(Airport, related_name='airports')
	company = models.ForeignKey(Company, related_name='flights')

	def __unicode__(self):
		return self.code+" - "+self.origin+"-"+self.destination+" - "+self.gate

	def get_absolute_url(self):
		return reverse('flight_detail', kwargs = {'pkr' : self.company.pk, 'pk' : self.pk})
