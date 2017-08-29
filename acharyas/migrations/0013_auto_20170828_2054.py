# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acharyas', '0012_auto_20170828_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centre',
            name='continent',
        ),
        migrations.AlterField(
            model_name='acharya',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Brni', 'Brni'), ('Br', 'Br'), ('Swami', 'Swami'), ('Swamini', 'Swamini'), ('Acharya', 'Acharya')], default='', max_length=100),
        ),
    ]