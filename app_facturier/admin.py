# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.


class DevisAdmin(admin.ModelAdmin):
    model = Devis

admin.site.register(Devis, DevisAdmin)



class ClientAdmin(admin.ModelAdmin):
    model = Client

admin.site.register(Client, ClientAdmin)



class ProfilInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilInline, )

admin.site.unregister(User)
admin.site.register( User, UserAdmin)
