# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20170630_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipecategory',
            name='level',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='lft',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='recipes.RecipeCategory'),
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='rght',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipecategory',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Περιγραφή'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text_eng',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Περιγραφή στα Eng'),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Περιγραφή'),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='text_eng',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Περιγραφή στα Eng'),
        ),
    ]
