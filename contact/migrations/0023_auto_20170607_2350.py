# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0022_auto_20170607_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 50, 21, 522216), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 50, 21, 521214), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
