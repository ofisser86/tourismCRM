# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_tour_tour_nmb'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]