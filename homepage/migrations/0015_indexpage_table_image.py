# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_tableopentimes_page_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='table_image',
            field=models.ImageField(null=True, upload_to=homepage.models.upload_photo, verbose_name='Είκονα Κλείσε Τραπέζι'),
        ),
    ]
