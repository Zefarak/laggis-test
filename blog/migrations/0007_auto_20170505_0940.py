# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 06:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170505_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 5, 9, 40, 12, 294546), verbose_name='Ημερομηνία Event/Παρουσίασης'),
        ),
    ]
