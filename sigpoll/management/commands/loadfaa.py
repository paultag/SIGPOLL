from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from sigpoll.models import Aircraft, Model

from contextlib import contextmanager
import argparse
import csv
import os


class Command(BaseCommand):
    help = 'Load an FAA data dump'
    CACHE = {}

    def add_arguments(self, parser):
        parser.add_argument(
            type=str,
            dest='folder',
            help='dump root'
        )

    def get_model(self, craft):
        name = craft['MFR MDL CODE']

        if name in self.CACHE:
            return self.CACHE[name]

        model = None
        try:
            model = Model.objects.get(id=name.strip())
        except Model.DoesNotExist:
            print("Unmatched model: {}".format(craft['MFR MDL CODE'].strip()))

        self.CACHE[name] = model
        return model

    def load_aircraft(self, name):
        with self.load_csv(name) as crafts:
            for craft in crafts:
                x = Aircraft(
                    tail_number=craft['N-NUMBER'].strip(),
                    model=self.get_model(craft),
                    id=craft['MODE S CODE HEX'].strip(),

                    status=craft['STATUS CODE'],
                    type=craft['TYPE AIRCRAFT'],

                    registrant_type=craft['TYPE REGISTRANT'],
                    registrant_name=craft['NAME'],
                    registrant_street=craft['STREET'],
                    registrant_street2=craft['STREET2'],
                    registrant_city=craft['CITY'],
                    registrant_state=craft['STATE'],
                    registrant_zipcode=craft['ZIP CODE'],
                    registrant_region=craft['REGION'],
                    registrant_county=craft['COUNTY'],
                    registrant_country=craft['COUNTRY'],
                )
                x.save()

    def load_models(self):
        with self.load_csv('ACFTREF.txt') as models:
            for model in models:
                x = Model(
                    id=model['CODE'],
                    manufacturer=model['MFR'].strip(),
                    name=model['MODEL'].strip())
                x.save()

    @contextmanager
    def load_csv(self, name):
        with open(os.path.join(self.root, name), 'r') as fd:
            yield csv.DictReader((x.replace('\ufeff', '') for x in fd))

    def handle(self, *args, **options):
        self.root = options['folder']
        with transaction.atomic():
            self.load_models()
            for flavor in ['MASTER',]:
                self.load_aircraft("{}.txt".format(flavor))
