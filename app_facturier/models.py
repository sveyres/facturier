# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entreprise = models.CharField(max_length=20)
    phone = models.IntegerField()
    siret = models.IntegerField()
    mail = models.CharField(max_length=20)
    adress_1 = models.CharField(max_length=20)
    adress_2 = models.CharField(max_length=20, verbose_name='adress_2')
    zipcode = models.IntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)


class Client(models.Model):
    entreprise = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    adress_1 = models.CharField(max_length=20)
    adress_2 = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __unicode__(self):
       return self.entreprise

class Devis(models.Model):
    client = models.ForeignKey(Client)
    profile = models.ForeignKey(Profile)
    date_creation = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=20)
    date_refusal = models.DateTimeField(null=True, blank=True)
    date_acceptance = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Devis"

class Facture(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, default = None)
    profile = models.ForeignKey(Profile, null=True, blank=True, default = None)
    date_creation = models.DateTimeField()
    ref = models.CharField(max_length=20)
    date_payment = models.DateTimeField(null=True, blank=True)

class LigneFacture(models.Model):
    facture= models.ForeignKey(Facture)
    designation = models.CharField(max_length=20)
    quantity = models.IntegerField()

class LigneDevis(models.Model):
    devis= models.ForeignKey(Devis)
    designation = models.CharField(max_length=20)
    quantity = models.IntegerField()
