# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturier', '0009_auto_20170623_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('DEVEC', 'Devis en cours'), ('FACEC', 'Facture en cours'), ('DVALI', 'Valid\xe9'), ('FPAYE', 'Valid\xe9')], max_length=150),
        ),
    ]
