# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from .fields import PhoneField
from django.core.validators import RegexValidator

class Centre(models.Model):
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = CountryField()
    postal_code = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return "%s (%s, %s)" % (self.name or '', self.state or '', self.country or '', )
    def get_acharyas(self):
        return ", ".join([str(p) for p in self.acharya.all()])

class Acharya(models.Model):
    SALUTATION_CHOICES = [
        ("Brni", "Brni"),
        ("Br", "Br"),
        ("Swami", "Swami"),
        ("Swamini", "Swamini"),
        ("Acharya", "Acharya"),
    ]
    profile_id = models.IntegerField(blank=True, null=True)
    salutation = models.CharField(max_length=100, choices=SALUTATION_CHOICES, blank=True, default='')
    name = models.CharField(max_length=100, null=False)
    dob = models.DateField('Date of birth', blank=True, null=True)
    centre = models.ManyToManyField(Centre, related_name='acharya', blank=True)
    admin_note = models.TextField(blank=True, null=True)
    biodata = models.TextField(blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    br_diksha_date = models.DateField('Brahmachari(ni) diksha date', blank=True, null=True)
    trained_under = models.ForeignKey("self", blank=True, null=True)
    chinmaya_id = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=20, validators=[phone_regex], blank=True) # validators should be a list
    def __str__(self):
        return "%s %s" % (self.salutation, self.name,)
    def centres(self):
        return ", ".join([str(p) for p in self.centre.all()])