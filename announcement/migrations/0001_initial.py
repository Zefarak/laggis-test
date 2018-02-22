# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 13:43
from __future__ import unicode_literals

import announcement.models
import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Τίτλος')),
                ('publish', models.DateTimeField(auto_now_add=True, verbose_name='Ημερομηνία Δημιουργίας')),
                ('image', models.ImageField(help_text='Width:300px, height:200px', null=True, upload_to=announcement.models.upload_file)),
                ('date_start', models.DateTimeField(default=datetime.datetime(2017, 4, 30, 16, 43, 0, 669932), verbose_name='Ημερομηνία Έναρξης')),
                ('date_expire', models.DateTimeField(default=datetime.datetime(2017, 4, 30, 16, 43, 0, 669932), verbose_name='Ημερομηνία Λήξης')),
                ('text', models.TextField(verbose_name='Περιγραφή')),
                ('active', models.BooleanField(default=True, verbose_name='Ορατό Στην Κεντρική σελίδα')),
            ],
            options={
                'ordering': ['date_expire'],
            },
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='tags',
            field=models.ManyToManyField(to='announcement.AnnouncementTag'),
        ),
    ]
