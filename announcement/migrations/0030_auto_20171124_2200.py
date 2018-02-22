# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 20:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0029_auto_20171124_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 0, 29, 253096), verbose_name='Ημερομηνία Λήξης'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 0, 29, 253096), verbose_name='Ημερομηνία Έναρξης'),
        ),
    ]
