# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturier', '0004_auto_20170622_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='price',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
