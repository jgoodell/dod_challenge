from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'dod_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/companies/', views.post_company),
    url(r'^/companies/(?P<company_id>[0-9]+)/$', views.get_company),
    url(r'^/companies/people/', views.post_person),
    url(r'^/companies/people/(?P<person_id>[0-9]+)/$', views.get_person),
    url(r'^/companies/people/email/', views.post_email),
    url(r'^/companies/people/email/(?P<email_id>[0-9]+)/$', views.get_email),
    url(r'^/companies/people/address/', views.post_address),
    url(r'^/companies/people/address/(?P<address_id>[0-9]+)/$', views.get_address),
    url(r'^/companies/people/phone/', views.post_phone),
    url(r'^/companies/people/phone/(?P<phone_id>[0-9]+)/$', views.get_phone),
]
