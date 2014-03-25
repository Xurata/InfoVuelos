
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iInfoVuelos.models import *

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	
	sobres = user.sobre_set.all() #preguntar!!!
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'sobres': sobres
		})
	output = template.render(variables)
	return HttpResponse(output)

def company_all(request):
	try:
		companies = Company.objects.all()
	except:
		raise Http404('User not found.')
	
	template = get_template('company.html')
	variables = Context({
		#'username': username,
		'companies': companies
		})
	output = template.render(variables)
	return HttpResponse(output)

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
