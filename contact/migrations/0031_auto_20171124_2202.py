# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0030_auto_20171124_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 2, 24, 428020), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 2, 24, 426520), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]