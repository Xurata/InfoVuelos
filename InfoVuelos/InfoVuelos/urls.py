from django.conf.urls import patterns, include, url
from iInfoVuelos.views import *
from django.views.generic import DetailView, ListView, UpdateView
from iInfoVuelos.forms import CompanyForm, FlightForm
from iInfoVuelos.views import CompanyCreate, FlightCreate, CompanyDetail, APICompanyList, \
								APICompanyDetail, APIFlightList, APIFlightDetail, delete_Company, \
								APICompanyReviewDetail, APICompanyReviewList
from iInfoVuelos.models import Airport, Flight, Company

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InfoVuelos.views.home', name='home'),
    # url(r'^InfoVuelos/', include('InfoVuelos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', mainpage, name ='Home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout'),
    
    # Airport list ex.: /airport
    url(r'^airport/$',
    	ListView.as_view(
    		queryset=Airport.objects.all(),
    		context_object_name='All_airport_list',
    		template_name='airport_all.html'),
    		name='airport_all'),
    
    # Company list  ex.: /company
    url(r'^company/$',
    	ListView.as_view(
    		queryset=Company.objects.all(),
    		context_object_name='All_company_list',
    		template_name='company_all.html'),
    		name='company_all'),
    
    # Flight list  ex.: /flight
    url(r'^flight/$',
    	ListView.as_view(
    		queryset=Flight.objects.all(),
    		context_object_name='All_flight_list',
    		template_name='flight_all.html'),
    		name='flight_all'),
    
    # Company details, ex.: /company/1			
    url(r'^company/(?P<pk>\d+)/$',
    	CompanyDetail.as_view(),
    	name='company_detail'),
    
    # Flight details, ex.: /flight/1			
    url(r'^company/(?P<pkr>\d+)/flight/(?P<pk>\d+)/$',
    	DetailView.as_view(
    	model = Flight,
    	template_name='flight_detail.html'),
    	name='flight_detail'),

	#Create a company, ex.: /company/create/
	url(r'^company/create/$',
		CompanyCreate.as_view(),
		name='company_create'),
	
	#Edit company details, ex.: /company/1/edit/
	url(r'^company/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = Company,
			template_name = 'forms.html',
			form_class = CompanyForm),
		name='company_edit'),

	#Create a flight, ex.: /company/1/flight/create
	url(r'^company/(?P<pk>\d+)/flight/create/$',
		FlightCreate.as_view(),
		name='flight_create'),

	#Edit company flight's details, ex.: /company/1/flight/1/edit/
	url(r'^company/(?P<pkr>\d+)/flight/(?P<pk>\d+)/edit/$',
		UpdateView.as_view(
			model = Flight,
			template_name = 'forms.html',
			form_class = FlightForm),
		name='flight_edit'),
	
	#Delete a Company ex.: company/1/delete
	url(r'^company/(?P<pk>[0-9]+)/delete/$', delete_Company, name='company_delete'),
	
	# Create a restaurant review using function, ex: /Company/1/reviews/create/
    url(r'^company/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
)		
# API Restfull
urlpatterns += patterns('',	
	url(r'^api/$','api_root'),	
	url(r'^api/company/$',	APICompanyList.as_view(), name='company_all'),	
	url(r'^api/company/(?P<pk>\d+)/$', APICompanyDetail.as_view(), name='company-detail'),	
	url(r'^api/flight/$', APIFlightList.as_view(), name='flight_all'),	
	url(r'^api/flight/(?P<pk>\d+)/$', APIFlightDetail.as_view(), name='flight-detail'),	
	url(r'^api/companyreviews/$', APICompanyReviewList.as_view(), name='companyreview-list'),	
	url(r'^api/companyreviews/(?P<pk>\d+)/$', APICompanyReviewDetail.as_view(),name='companyreview-detail'),							
)
