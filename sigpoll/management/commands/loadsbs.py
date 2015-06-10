from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from sigpoll.parser import sbs_to_db
import argparse


def load(stream):
    count = {'count': 0}
    with transaction.atomic():
        for line in stream:
            for data in sbs_to_db(line):
                count['count'] += 1
                data.save()
    return count



class Command(BaseCommand):
    help = 'Load an SBS1 log'

    def add_arguments(self, parser):
        parser.add_argument(
            type=argparse.FileType('r'),
            dest='inputfile',
            help='Name of file to be imported'
        )

    def handle(self, *args, **options):
        stream = options['inputfile']
        report = load(stream)
        print(report)
