# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturier', '0007_auto_20170623_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='proposal',
            name='ref',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
