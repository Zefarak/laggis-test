# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0023_auto_20170607_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 56, 54, 54037), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 56, 54, 52536), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]