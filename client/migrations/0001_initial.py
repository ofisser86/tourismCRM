# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 13:41
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
                ('middle_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Middle name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('document_scan', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ClientDocumentScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='client_doc/')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('client_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
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
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phones',
            },
        ),
    ]
