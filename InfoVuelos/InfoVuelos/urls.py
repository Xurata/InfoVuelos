from django.conf.urls import patterns, include, url
from iInfoVuelos.views import *

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

)
