# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20170505_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='icon',
            field=models.ImageField(help_text='260*350', null=True, upload_to=homepage.models.upload_photo, verbose_name='Φωτογραφία'),
        ),
    ]