# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170502_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='show_first_page',
        ),
        migrations.RemoveField(
            model_name='recipecategory',
            name='black_image',
        ),
        migrations.RemoveField(
            model_name='recipecategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='recipecategory',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipecategory',
            name='is_first_page',
        ),
    ]
