# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-05 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practicals', '0005_auto_20161105_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
    ]
