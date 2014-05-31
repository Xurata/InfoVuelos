from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

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

	def averageRating(self):
		ratingSum = 0.0
		for review in self.companyreview_set.all():
			ratingSum += review.rating
		reviewCount = self.companyreview_set.count()
		return ratingSum / reviewCount

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

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class CompanyReview(Review):
    company = models.ForeignKey(Company)
