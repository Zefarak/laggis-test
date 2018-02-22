# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 20:00
from __future__ import unicode_literals

import blog.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20171124_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='Το μέγεθος πρέπει να είναι μέχρι 0,5 mb', upload_to=blog.models.upload_file, validators=[blog.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords_eng',
            field=models.CharField(blank=True, max_length=100, verbose_name='English Keywords'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_description_eng',
            field=models.CharField(blank=True, max_length=100, verbose_name='English Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='seo',
            field=models.CharField(blank=True, max_length=100, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 0, 29, 249575), verbose_name='Ημερομηνία Event/Παρουσίασης'),
        ),
    ]
