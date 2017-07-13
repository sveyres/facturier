from django.core.management.base import BaseCommand
from app_facturier.models import *
import csv
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        Proposal.objects.all().delete()
        with open('app_facturier/export_facturier.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()

            for row in csvreader:
                id, customer, status, creation_date, update_date, product, price, qty = row
                customer = Client.objects.get(id=customer)
                creation_date = datetime.strptime(creation_date, '%d/%m/%y %H:%M')

                profile, profile_created = Profile.objects.get_or_create(
                    user_id = 1
                )

                proposal, proposal_created = Proposal.objects.get_or_create(
                    profile_id = 0,
                    ref = id,
                    client = customer,
                )
                proposal.date_creation = creation_date

                if status == "STANDBY":
                    if id.startswith("D"):
                        proposal.status = "DEVEC"
                    else : #id.startswith("F")
                        proposal.status = "FACEC"
                        proposal.date_acceptance = creation_date

                elif status == "LOST":
                    update_date = datetime.strptime(update_date, '%d/%m/%y %H:%M')
                    proposal.date_refusal = update_date
                    proposal.status = "DPERD"

                elif status == "PAID":
                    update_date = datetime.strptime(update_date, '%d/%m/%y %H:%M')
                    proposal.date_payment = update_date
                    proposal.status = "FPAYE"

                line, line_created = Line.objects.get_or_create(
                    proposal =  Proposal.objects.get(ref=id),
                    designation = product,
                    price = price,
                    quantity = qty
                )

                proposal.save()
                line.save()
