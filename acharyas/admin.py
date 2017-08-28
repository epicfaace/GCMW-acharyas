# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Centre, Acharya
from django.forms import Textarea
from django.db import models

class AcharyaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_centres', 'joined_date')
    fieldsets =  (
        ('Basic info', {
            'fields': ('salutation', 'name', 'centre', 'biodata')
        }),
        ('Dates', {
            'fields': ('dob', 'joined_date', 'br_diksha_date')
        }),
        ('Metadata', {
            'fields': ('trained_under', 'profile_id', 'chinmaya_id', 'admin_note')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':60})},
    }
class CentreAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country')

admin.site.register(Acharya, AcharyaAdmin)
admin.site.register(Centre)