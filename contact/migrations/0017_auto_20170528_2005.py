# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 17:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_auto_20170528_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservationinfo',
            options={'verbose_name_plural': '8. Πληροφορίες σελίδας Reservation'},
        ),
        migrations.AddField(
            model_name='reservationinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 28, 20, 5, 16, 503892), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 28, 20, 5, 16, 501892), verbose_name='Ημερομηνία Δημιουργίας'),
        ),
    ]