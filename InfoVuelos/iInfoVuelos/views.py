from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iInfoVuelos.models import *
from django.views.generic import DetailView
from forms import CompanyForm, FlightForm
from django.views.generic.edit import CreateView
from serializers import CompanySerializer, FlightSerializer, CompanyReviewSerializer
from django.http import HttpResponseRedirect

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'InfoVuelos App',
		'pagetitle': 'Welcome to the InfoVuelos application',
		'contentbody': 'Managing flight information',
		'user':	request.user
	})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	
	companies = user.company_set.all() 
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'companies': companies
		})
	output = template.render(variables)
	return HttpResponse(output)

class CompanyDetail(DetailView):
	model = Company
	template_name= 'company_detail.html'
	
	def get_context_data(self,**kwargs):
		context	= super(CompanyDetail,self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = CompanyReview.RATING_CHOICES
		return context
	
class CompanyCreate(CreateView):
	model = Company
	template_name = 'forms.html'
	form_class = CompanyForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CompanyCreate, self).form_valid(form)	

class FlightCreate(CreateView):
	model = Flight
	template_name = 'forms.html'
	form_class = FlightForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.company = Company.objects.get(id=self.kwargs['pk'])
		return super(FlightCreate, self).form_valid(form)
		
@login_required()
def delete_Company(request, pk):
    if request.user in User.objects.filter(groups__name='name'):
		raise PermissionDenied
    get_object_or_404(Company, pk=pk).delete()
    return HttpResponseRedirect("/company/")

@login_required()
def review(request, pk):
    company = get_object_or_404(Company, pk=pk)
    new_review = CompanyReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        company=company)
    new_review.save()
    return HttpResponseRedirect(reverse('company_detail', args=(company.id,)))		

# API InfoVuelos

class APICompanyList(generics.ListCreateAPIView):
	model = Company
	serializer_class = CompanySerializer

class APICompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Company
	serializer_class = CompanySerializer

class APIFlightList(generics.ListCreateAPIView):
	model = Flight
	serializer_class = FlightSerializer 

class APIFlightDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Flight
	serializer_class = FlightSerializer

class APICompanyReviewList(generics.ListCreateAPIView):
    model = CompanyReview
    serializer_class = CompanyReviewSerializer

class APICompanyReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    model = CompanyReview
    serializer_class = CompanyReviewSerializer	
