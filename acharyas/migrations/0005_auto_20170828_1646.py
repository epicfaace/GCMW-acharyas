# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acharyas', '0004_auto_20170828_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acharya',
            name='centre',
            field=models.ManyToManyField(blank=True, related_name='acharya', to='acharyas.Centre'),
        ),
    ]