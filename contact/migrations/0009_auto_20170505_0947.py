# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 06:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20170505_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 47, 15, 602977), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 47, 15, 601476), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Τηλέφωνο'),
        ),
    ]
