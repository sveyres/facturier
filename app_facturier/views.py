# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from models import *
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')

class DevisListView(ListView):
    model = Proposal
    context_object_name = "proposals"
    template_name = "app_facturier/tdb.html"

class TresListView(ListView):
    model = Proposal
    context_object_name = "proposals"
    template_name = "app_facturier/tdb.html"

class DevisDetailView(DetailView):
    model = Proposal
    slug_field = "ref"
    template_name = "app_facturier/devis_detail.html"

class DevisCreateView(CreateView):
    model = Proposal
    fields = ('client', 'profile', 'status', 'ref')
    template_name = "app_facturier/devis_create.html"
    success_url = reverse_lazy('tdb')

    def get_context_data(self):
        context = CreateView.get_context_data(self)
        context["line_formset"] = lineInlineFormset()
        return context

    def form_valid(self, form):
        line_resp = CreateView.form_valid(self, form)
        line_formset = lineInlineFormset(self.request.POST, instance=self.object)

        if line_formset.is_valid():
            line_formset.save()

        return line_resp

class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    template_name = "app_facturier/client_create.html"
    success_url = reverse_lazy('devis-create')

class LineCreateView(CreateView):
    model = Line
    fields = "__all__"
    template_name = "app_facturier/line_create.html"
    success_url = reverse_lazy('devis-create')

class DevisUpdateView(UpdateView):
    model = Proposal
    slug_field = "ref"
    fields = ('client', 'profile', 'status', 'ref')

    def get_success_url(self):
        return reverse("devis-detail", kwargs={'slug': self.object.ref})


class DevisDeleteView(DeleteView):
    model = Proposal
    slug_field = "ref"
    success_url = reverse_lazy('tdb')
