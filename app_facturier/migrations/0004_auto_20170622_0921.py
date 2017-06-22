# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_facturier', '0003_auto_20170620_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigneDevis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('devis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturier.Devis')),
            ],
        ),
        migrations.CreateModel(
            name='LigneFacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_facturier.Facture')),
            ],
        ),
        migrations.RemoveField(
            model_name='contain',
            name='devis',
        ),
        migrations.RemoveField(
            model_name='contain',
            name='facture',
        ),
        migrations.DeleteModel(
            name='contain',
        ),
    ]