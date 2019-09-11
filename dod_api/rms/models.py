from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=256)


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Email(models.Model):
    address = models.CharField(max_length=128)


class Address(models.Model):
    number = models.CharField(max_length=128)
    stree = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    country = models.CharField(max_length=128)


class Phone(models.Model):
    number = models.CharField(max_length=128)
