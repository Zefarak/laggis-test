# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170528_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 28, 20, 10, 7, 523579), verbose_name='Ημερομηνία Event/Παρουσίασης'),
        ),
    ]