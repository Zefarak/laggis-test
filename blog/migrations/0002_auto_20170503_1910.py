# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 16:10
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_file, verbose_name='Image - not used atm'),
        ),
    ]
