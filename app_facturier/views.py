# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from models import *
from .forms import *
import datetime

def homepage(request):
    return render(request, 'homepage.html')


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    template_name = "app_facturier/client_create.html"
    success_url = reverse_lazy('proposal-create')


class ClientListView(ListView):
    model = Client
    context_object_name = "clients"




class ProposalDetailView(DetailView):
    model = Proposal
    slug_field = "ref"
    template_name = "app_facturier/proposal_detail.html"

class ProposalCreateView(CreateView):
    model = Proposal
    fields = ('client', 'profile', 'status', 'ref')
    template_name = "app_facturier/proposal_create.html"
    success_url = reverse_lazy('tdb')

    def get_context_data(self, form=None):
        context = CreateView.get_context_data(self)
        context["line_formset"] = lineInlineFormset()
        return context

    def form_valid(self, form):
        line_resp = CreateView.form_valid(self, form)
        line_formset = lineInlineFormset(self.request.POST, instance=self.object)

        if line_formset.is_valid():
            line_formset.save()

        return line_resp

class ProposalListView(ListView):
    # context_object_name = "proposals"
    model = Proposal
    template_name = "app_facturier/tdb.html"

    def get_context_data(self):
        context = ListView.get_context_data(self)
        context['devEnCours'] = Proposal.objects.filter(status = "DEVEC")
        context['factEnCours'] = Proposal.objects.filter(status = "FACEC")
        return context

class ProposalUpdateView(UpdateView):
    model = Proposal
    slug_field = "ref"
    fields = "__all__"

    def get_success_url(self):
        return reverse("proposal-detail", kwargs={'slug': self.object.ref})

class ProposalDeleteView(DeleteView):
    model = Proposal
    slug_field = "ref"
    success_url = reverse_lazy('tdb')




class LineCreateView(CreateView):
    model = Line
    fields = "__all__"
    template_name = "app_facturier/line_create.html"
    success_url = reverse_lazy('proposal-create')



class TresListView(ListView):
    model = Proposal
    # context_object_name = "proposals"
    template_name = "app_facturier/tresorerie.html"

    def get_context_data(self):
        context = ListView.get_context_data(self)
        fpayee = Proposal.objects.filter(status = "FPAYE")
        context['factPayee'] = fpayee
        total = 0
        for f in fpayee:
            total += f.amount()
        context['total'] = total

        return context

class ArchListView(ListView):
    model = Proposal
    # context_object_name = "proposals"
    template_name = "app_facturier/archives.html"

    def get_context_data(self):
        context = ListView.get_context_data(self)
        context['devPerdus'] = Proposal.objects.filter(status = "DPERD")
        context['factPayee'] = Proposal.objects.filter(status = "FPAYE")
        return context







def change_status(request, ref):
    now = datetime.datetime.now()
    prop = Proposal.objects.get(ref=ref)
    prop.status = "FACEC"
    prop.date_acceptance = now
    prop.save()
    # context = {
    #     "ref" : prop.ref
    # }
    return redirect('tdb')
    # return render(request, "app_facturier/proposal_detail.html", context)

def arch_proposal(request, ref):
    now = datetime.datetime.now()
    prop = Proposal.objects.get(ref=ref)
    if prop.status == "DEVEC":
        prop.status = "DPERD"
        prop.date_refusal = now
    else:
        prop.status = "FPAYE"
        prop.date_payment = now
    prop.save()
    context = {
        "proposal" : prop
    }
    return redirect('archives')
