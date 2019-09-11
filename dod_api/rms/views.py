from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def get_company(request):
    return HttpResponse('company')


def post_company(request):
    return HttpResponse('company')


def get_person(request):
    return HttpResponse('person')


def post_person(request):
    return HttpResponse('person')


def get_email(request):
    return HttpResponse('email')


def post_email(request):
    return HttpResponse('email')


def get_address(request):
    return HttpResponse('address')


def post_address(request):
    return HttpResponse('address')


def get_phone(request):
    return HttpResponse('phone')


def post_phone(request):
    return HttpResponse('phone')
