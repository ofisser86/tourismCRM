# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('middle_name', models.CharField(max_length=32, verbose_name='Middle name')),
                ('client_city', models.CharField(max_length=32, verbose_name='City')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('email_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Client')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone')),
                ('phone_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Client')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
            },
        ),
    ]
