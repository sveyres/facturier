# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enterprise = models.CharField(max_length=20)
    phone = models.IntegerField()
    siret = models.IntegerField()
    mail = models.CharField(max_length=20)
    adress_1 = models.CharField(max_length=20)
    adress_2 = models.CharField(max_length=20, verbose_name='adress_2')
    zipcode = models.IntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __unicode__(self):
       return self.enterprise

class Client(models.Model):
    enterprise = models.CharField(max_length=20)
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
       return self.enterprise

class Status(models.Model):
    label = models.CharField(max_length=20)

    def __unicode__(self):
       return self.label

    class Meta:
        verbose_name_plural = "Status"

STATUS_CHOICES = (
    ("DEVEC", 'Devis en cours'),
    ("FACEC", 'Facture en cours'),
    ("DPERD", 'Perdu'),
    ("FPAYE", 'Payé'),
)

class Proposal(models.Model):
    client = models.ForeignKey(Client)
    profile = models.ForeignKey(Profile)
    # status = models.ForeignKey(Status)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES)
    ref = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_refusal = models.DateTimeField(null=True, blank=True)
    date_acceptance = models.DateTimeField(null=True, blank=True)
    date_payment = models.DateTimeField(null=True, blank=True)
    mail_reminder_date = models.DateTimeField(null=True, blank=True)

    def amount(self):
        result = 0
        for l in self.line_set.all():
            result += l.quantity * l.price
        return result

    def __unicode__(self):
       return self.ref

class Line(models.Model):
    proposal = models.ForeignKey(Proposal)
    price = models.IntegerField()
    designation = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __unicode__(self):
       return self.designation
