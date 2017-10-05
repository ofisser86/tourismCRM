# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='email_client',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='phone_client',
        ),
        migrations.AddField(
            model_name='client',
            name='client_email',
            field=models.ForeignKey(default=132, on_delete=django.db.models.deletion.CASCADE, to='crm.Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='client_phone',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='crm.Phone'),
            preserve_default=False,
        ),
    ]