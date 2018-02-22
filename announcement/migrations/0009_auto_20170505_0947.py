# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 06:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0008_auto_20170505_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 47, 15, 592476), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 47, 15, 592476), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]
