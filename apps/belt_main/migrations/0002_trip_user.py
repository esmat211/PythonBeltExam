# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160819_0942'),
        ('belt_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tripuser', to='registration.User'),
            preserve_default=False,
        ),
    ]
