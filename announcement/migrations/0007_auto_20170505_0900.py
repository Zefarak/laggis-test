# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 06:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_auto_20170505_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 0, 45, 818169), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 0, 45, 818169), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]