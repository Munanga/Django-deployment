# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 01:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='date',
        ),
    ]
