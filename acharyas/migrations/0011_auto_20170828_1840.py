# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acharyas', '0010_acharya_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acharya',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]