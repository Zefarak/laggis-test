# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20170608_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '2. Διαχείριση Κινούμενου Banner'},
        ),
        migrations.AlterModelOptions(
            name='blogpageinfo',
            options={'verbose_name_plural': '6. Seo Σελίδας Blog'},
        ),
        migrations.AlterModelOptions(
            name='indexpage',
            options={'verbose_name_plural': '1. Διαχείριση Αρχικής Σελίδας'},
        ),
        migrations.AlterModelOptions(
            name='menupageinfo',
            options={'verbose_name_plural': '5. Seo Σελίδας Menu'},
        ),
        migrations.AlterModelOptions(
            name='openhours',
            options={'ordering': ['order_by'], 'verbose_name_plural': '3. Διαχείριση Ωρών Λειτουργίας'},
        ),
        migrations.AlterModelOptions(
            name='tableopentimes',
            options={'verbose_name_plural': '4. Διαχείριση Πίνακα Ωρών'},
        ),
        migrations.AddField(
            model_name='indexpage',
            name='color_menu_hover',
            field=models.CharField(blank=True, default='#e3e3e3', help_text='Εάν το αφήσεις κενο παίρωει το αρχικό', max_length=20, null=True, verbose_name='Χρώμα menu επιλεγμένο'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='color_menu_li',
            field=models.CharField(blank=True, default='#e3e3e3', help_text='Εάν το αφήσεις κενο παίρωει το αρχικό', max_length=20, null=True, verbose_name='Χρώμα menu'),
        ),
        migrations.AlterField(
            model_name='menupageinfo',
            name='catalogue',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.models.upload_photo, verbose_name='Φωτογραφία καταλόγου'),
        ),
        migrations.AlterField(
            model_name='menupageinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=homepage.models.upload_photo, verbose_name='Banner photo'),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='close',
            field=models.CharField(max_length=10, verbose_name='κλείνουμε.'),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='open',
            field=models.CharField(max_length=10, verbose_name='Ανοίγουμε.'),
        ),
        migrations.AlterField(
            model_name='tableopentimes',
            name='times',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tableopentimes',
            name='title_eng',
            field=models.CharField(max_length=30),
        ),
    ]
