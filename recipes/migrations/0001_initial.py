# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-30 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, verbose_name='Ονομασία')),
                ('title_eng', models.CharField(max_length=100, verbose_name='Ονομασία στα Eng')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Εικόνα ')),
                ('black_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Σκίτσο')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Περιγραφή')),
                ('text_eng', models.TextField(blank=True, null=True, verbose_name='Περιγραφή στα Eng')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή')),
                ('slug', models.CharField(blank=True, max_length=160, null=True)),
                ('show_first_page', models.BooleanField(default=True, verbose_name='Εμφάνιση στο Μενού στην Αρχική Σελίδα')),
                ('is_special_item', models.BooleanField(default=False, verbose_name='Εμφάνιση στα Special στην Αρχική Σελίδα')),
                ('seo_title', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_keywords', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_title_eng', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description_eng', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_keywords_eng', models.CharField(blank=True, max_length=160, null=True)),
                ('by_order', models.IntegerField(default=1, verbose_name='Ταξινόμηση')),
            ],
            options={
                'verbose_name_plural': 'Συνταγές',
                'ordering': ['by_order'],
            },
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, verbose_name='Όνομασια')),
                ('title_eng', models.CharField(max_length=100, verbose_name='Όνομασια στα Eng')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Εικόνα')),
                ('black_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Σκίτσο')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Περιγραφή')),
                ('text_eng', models.TextField(blank=True, null=True, verbose_name='Περιγραφή στα Eng')),
                ('is_first_page', models.BooleanField(default=True, verbose_name='Εμφάνιση στην Αρχική Σελίδα')),
                ('slug', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_keywords', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_title_eng', models.CharField(blank=True, max_length=60, null=True)),
                ('seo_description_eng', models.CharField(blank=True, max_length=160, null=True)),
                ('seo_keywords_eng', models.CharField(blank=True, max_length=160, null=True)),
                ('by_order', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Κατηγορίες Συνταγών',
                'ordering': ['by_order'],
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.RecipeCategory', verbose_name='Κατηγορία'),
        ),
    ]