# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 16:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20170502_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 19, 10, 49, 394601), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 19, 10, 49, 393101), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
