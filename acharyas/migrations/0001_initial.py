# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acharya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.CharField(blank=True, default='', max_length=100)),
                ('salutation', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('joined_date', models.DateField()),
                ('br_diksha_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address_line_1', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postal_code', models.CharField(blank=True, max_length=10)),
                ('continent', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='acharya',
            name='centre',
            field=models.ManyToManyField(related_name='acharya', to='acharyas.Centre'),
        ),
        migrations.AddField(
            model_name='acharya',
            name='trained_under',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acharyas.Acharya'),
        ),
    ]
