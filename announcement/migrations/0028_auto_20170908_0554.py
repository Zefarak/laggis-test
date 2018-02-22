# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 05:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0027_auto_20170630_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 8, 5, 54, 16, 672334), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 8, 5, 54, 16, 672226), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]
