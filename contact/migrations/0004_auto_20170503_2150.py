# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20170503_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 21, 50, 17, 807212), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 21, 50, 17, 806212), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]