# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 18:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_auto_20170503_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 21, 50, 17, 803711), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 21, 50, 17, 803711), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]