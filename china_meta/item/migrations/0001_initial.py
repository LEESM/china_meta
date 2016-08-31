# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=100)),
                ('source_url', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('delivery', models.CharField(max_length=100)),
                ('additional_benefit', models.CharField(max_length=100)),
            ],
        ),
    ]
