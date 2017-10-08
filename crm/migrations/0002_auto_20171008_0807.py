# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_in_tour',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_in_tour',
        ),
        migrations.AddField(
            model_name='tour',
            name='country',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='crm.Country'),
        ),
        migrations.AddField(
            model_name='tour',
            name='hotel',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='crm.Hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_status',
            field=models.BooleanField(default=True, verbose_name='Status is available'),
        ),
    ]
