from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'dod_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/companies/', views.companies),
    url(r'^/companies/(?P<company_id>[0-9]+)/$', views.company),
    url(r'^/companies/people/', views.people),
    url(r'^/companies/people/(?P<person_id>[0-9]+)/$', views.person),
    url(r'^/companies/people/email/', views.emails),
    url(r'^/companies/people/email/(?P<email_id>[0-9]+)/$', views.email),
    url(r'^/companies/people/address/', views.addresses),
    url(r'^/companies/people/address/(?P<address_id>[0-9]+)/$', views.address),
    url(r'^/companies/people/phone/', views.phone_numbers),
    url(r'^/companies/people/phone/(?P<phone_id>[0-9]+)/$', views.phone_number),
]
