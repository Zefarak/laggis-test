# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 06:16
from __future__ import unicode_literals

import blog.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
#import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20170908_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.upload_file_gallery, validators=[blog.models.validate_image])),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='keywords_eng',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description_eng',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='Το μέγεθος πρέπει να είναι μέχρι 0,5 mb', upload_to=blog.models.upload_file, validators=[blog.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 8, 16, 57, 581280), verbose_name='Ημερομηνία Event/Παρουσίασης'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='post_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
