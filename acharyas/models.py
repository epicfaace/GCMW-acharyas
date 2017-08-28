# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField

class Centre(models.Model):
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = CountryField()
    postal_code = models.CharField(max_length=10, blank=True)
    continent = models.CharField(max_length=100, blank=True)

class Acharya(models.Model):
    profile_id = models.CharField(max_length=100, blank=True, default='')
    salutation = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100)
    dob = models.DateField()
    centre = models.ManyToManyField(Centre, related_name='acharya')
    joined_date = models.DateField()
    br_diksha_date = models.DateField()
    trained_under = models.ForeignKey("self")
    def __str__(self):
        return self.name