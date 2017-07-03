from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^tdb$', DevisListView.as_view(), name="tdb"),
    url(r'^devis/new/$', DevisCreateView.as_view(), name="devis-create"),
    url(r'^(?P<slug>[\w-]+)/edit$', DevisUpdateView.as_view(), name="devis-validate"),
    url(r'^(?P<slug>[\w-]+)/delete$', DevisDeleteView.as_view(), name="devis-delete"),
    url(r'^client/new/$', ClientCreateView.as_view(), name="client-create"),
    url(r'^line/new/$', LineCreateView.as_view(), name="line-create"),
    url(r'^(?P<slug>[\w-]+)$', DevisDetailView.as_view(), name="devis-detail"),
    url(r'^tresorerie/$', TresListView.as_view(), name="tresorerie"),
]
