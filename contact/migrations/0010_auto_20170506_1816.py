# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20170505_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 6, 18, 16, 56, 373894), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 6, 18, 16, 56, 372394), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
