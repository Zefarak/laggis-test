# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_auto_20170525_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 28, 19, 19, 21, 168400), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 28, 19, 19, 21, 166900), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]
