from .models import *
from django.forms import inlineformset_factory

lineInlineFormset = inlineformset_factory(Proposal, Line, fields=['designation', 'quantity', 'price'] , min_num =1, extra =1)
