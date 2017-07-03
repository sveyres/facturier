# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.




class LineInline(admin.TabularInline):
    model = Line

class ProposalAdmin(admin.ModelAdmin):
    model = Proposal
    inlines = [
        LineInline,
    ]

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Line)


class ClientAdmin(admin.ModelAdmin):
    model = Client

admin.site.register(Client, ClientAdmin)

class StatusAdmin(admin.ModelAdmin):
    model = Status

admin.site.register(Status, StatusAdmin)


class ProfilInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilInline, )

admin.site.unregister(User)
admin.site.register( User, UserAdmin)
