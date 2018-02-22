# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0022_auto_20170607_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 50, 21, 518218), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 7, 23, 50, 21, 517719), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]
