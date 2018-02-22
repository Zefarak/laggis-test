# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 13:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 4, 30, 16, 43, 0, 673933), verbose_name='Ημερομηνία Δημιουργίας')),
                ('name', models.CharField(max_length=255, verbose_name='Ονοματεπώνυμο')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Τηλέφωνο')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('people', models.IntegerField(default=2, verbose_name="'Ατομα")),
                ('message', models.TextField(blank=True, null=True, verbose_name='Μήνυμα')),
                ('resever_date', models.DateField(verbose_name='Ημερομηνία Κράτησης')),
                ('time', models.CharField(max_length=15, verbose_name="'Ωρα Κράτησης")),
                ('is_readed', models.BooleanField(default=False, verbose_name='Το έχεις δει;')),
            ],
            options={
                'verbose_name_plural': 'Κρατήσεις',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 4, 30, 16, 43, 0, 672934), verbose_name='Ημερομηνία Δημιουργίας')),
                ('name', models.CharField(max_length=255, verbose_name='Ονοματεπώνυμο')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Τηλέφωνο')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True, verbose_name='Μήνυμα')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Το έχεις δει;')),
            ],
            options={
                'verbose_name_plural': 'Επικοινωνία',
            },
        ),
        migrations.CreateModel(
            name='ContactInfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.CharField(default='Ωρες Λειτουργίας', max_length=160, verbose_name='Τίτλος, Ωρες Λειτουργίας στα Ελληνικά')),
                ('address', models.CharField(default='Διεύθυνση', max_length=160, verbose_name='Τίτλος Διεύθυνση στα Ελληνικά')),
                ('address_text', models.TextField(default='', verbose_name='Κείμενο Διεύθυνση στα Ελληνικά')),
                ('support', models.CharField(default='Support', max_length=160, verbose_name='Τίτλος Ωρες support στα Ελληνικά')),
                ('support_text', models.TextField(default='', verbose_name='Κείμενο support στα Ελληνικά')),
                ('open_time_eng', models.CharField(default='Ωρες Λειτουργίας', max_length=160, verbose_name='Τίτλος, Ωρες Λειτουργίας στα Αγγλικά')),
                ('address_eng', models.CharField(default='Διεύθυνση', max_length=160, verbose_name='Τίτλος Διεύθυνση στα Αγγλικά')),
                ('address_text_eng', models.TextField(default='', verbose_name='Κείμενο Διεύθυνση στα Αγγλικά')),
                ('support_eng', models.CharField(default='Support', max_length=160, verbose_name='Τίτλος Ωρες support στα Αγγλικά')),
                ('support_text_eng', models.TextField(default='', verbose_name='Κείμενο support στα Αγγλικά')),
            ],
            options={
                'verbose_name_plural': 'Πληροφορίες Contact Page',
            },
        ),
        migrations.CreateModel(
            name='ReservationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_title', models.CharField(default='Αριστερός τίτλος στα Ελληνικά', max_length=160)),
                ('left_text', models.TextField(default='Αριστερή περιγραφή στα Ελληνικά')),
                ('right_title', models.CharField(default='Δεξιός τίτλος στα Ελληνικά', max_length=160)),
                ('right_text', models.TextField(default='Δεξιά περιγραφή στα Ελληνικά', max_length=160)),
                ('banner_title', models.CharField(default='Τίτλος Banner στα Ελληνικά', max_length=160)),
                ('banner_text', models.TextField(default='Περιγραφή στα Ελληνικά')),
                ('left_title_eng', models.CharField(default='Αριστερός τίτλος στα Αγγλικά', max_length=160)),
                ('left_text_eng', models.TextField(default='Αριστερή περιγραφή στα Αγγλικά')),
                ('right_title_eng', models.CharField(default='Δεξιός τίτλος στα Αγγλικά', max_length=160)),
                ('right_text_eng', models.TextField(default='Δεξιά περιγραφή στα Αγγλικά', max_length=160)),
                ('banner_title_eng', models.CharField(default='Τίτλος Banner στα Αγγλικά', max_length=160)),
                ('banner_text_eng', models.TextField(default='Περιγραφή στα Αγγλικά')),
            ],
        ),
    ]
