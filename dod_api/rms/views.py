from django.http import HttpResponse
from django.shortcuts import render

from . import utils

# Create your views here.

@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def company(request):
    return HttpResponse('company')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def companies(request):
    return HttpResponse('companies')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def person(request):
    return HttpResponse('person')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def people(request):
    return HttpResponse('people')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def email(request):
    return HttpResponse('email')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def emails(request):
    return HttpResponse('emails')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def address(request):
    return HttpResponse('address')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def addresses(request):
    return HttpResponse('addresses')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def phone_number(request):
    return HttpResponse('phone_nmber')


@utils.negotiate_types(content_types=['application/json','application/xml'],
                       accept_types=['application/json','application/xml'])
def phone_numbers(request):
    return HttpResponse('phone_numbers')
