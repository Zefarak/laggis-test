# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 03:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0014_auto_20170524_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 6, 27, 59, 35629), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 6, 27, 59, 34097), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
