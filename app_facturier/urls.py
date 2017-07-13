from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^devis/new/$', ProposalCreateView.as_view(), name="proposal-create"),
    url(r'^line/new/$', LineCreateView.as_view(), name="line-create"),
    url(r'^tdb$', ProposalListView.as_view(), name="tdb"),
    url(r'^client/new/$', ClientCreateView.as_view(), name="client-create"),
    url(r'^(?P<slug>[\w-]+)$', ProposalDetailView.as_view(), name="proposal-detail"),
    url(r'^(?P<slug>[\w-]+)/edit$', ProposalUpdateView.as_view(), name="proposal-validate"),
    url(r'^(?P<slug>[\w-]+)/delete$', ProposalDeleteView.as_view(), name="proposal-delete"),
    url(r'^liste/clients/$', ClientListView.as_view(), name="list-clients"),
    url(r'^tresorerie/$', TresListView.as_view(), name="tresorerie"),
    url(r'^archives/$', ArchListView.as_view(), name="archives"),
    url(r'^(?P<ref>[\w-]+)/change$', change_status, name="proposal-change"),
    url(r'^(?P<ref>[\w-]+)/arch$', arch_proposal, name="proposal-arch"),
]
