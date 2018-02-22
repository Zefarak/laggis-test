# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_auto_20170503_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 7, 49, 15, 15014), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 4, 7, 49, 15, 15014), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]