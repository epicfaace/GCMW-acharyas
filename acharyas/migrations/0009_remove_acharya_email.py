# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 22:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acharyas', '0008_acharya_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acharya',
            name='email',
        ),
    ]
