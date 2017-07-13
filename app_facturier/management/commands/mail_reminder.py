from django.core.management.base import BaseCommand
from app_facturier.models import *
from datetime import datetime, timedelta
from django.core.mail import send_mail

class Command(BaseCommand):

    def handle(self, *args, **options):
        now = datetime.now()
        proposals = Proposal.objects.all()

        for proposal in proposals :
            clientMail = proposal.client.mail
            ref = proposal.ref
            amount = str(proposal.amount())

            if proposal.mail_reminder_date == None  :
                if proposal.status == "DEVEC":
                    if now - proposal.date_creation > timedelta(days = 30):
                        proposal.mail_reminder_date = now

                        send_mail(
                            'Devis '+ref+' en attente de confirmation',
                            'Faudrait penser a valider le devis '+ref,
                            'frommoi@example.com',
                            [clientMail],
                            fail_silently=False,
                        )
                if proposal.status == "FACEC":
                    if now - proposal.date_acceptance > timedelta(days = 30):
                        proposal.mail_reminder_date = now

                        send_mail(
                            'Facture '+ref+' en attente de paiement',
                            "J'attends toujours mes "+amount+" euros",
                            'frommoi@example.com',
                            [clientMail],
                            fail_silently=False,
                        )
            else :
                if now - proposal.mail_reminder_date > timedelta(days = 15):
                    if proposal.status == "DEVEC":
                        proposal.mail_reminder_date = now
                        send_mail(
                            'Devis '+ref+' en attente de confirmation',
                            'Faudrait penser a valider le devis '+ref,
                            'frommoi@example.com',
                            [clientMail],
                            fail_silently=False,
                        )

                    if proposal.status == "FACEC":
                        proposal.mail_reminder_date = now

                        send_mail(
                            'Facture '+ref+' en attente de paiement',
                            "J'attends toujours mes "+amount+" euros",
                            'frommoi@example.com',
                            [clientMail],
                            fail_silently=False,
                        )

            proposal.save()
