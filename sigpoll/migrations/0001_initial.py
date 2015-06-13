# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=6)),
                ('tail_number', models.CharField(blank=True, db_index=True, max_length=32)),
                ('type', models.CharField(choices=[('1', 'Glider'), ('2', 'Balloon'), ('3', 'Blimp/Dirigible'), ('4', 'Fixed wing single engine'), ('5', 'Fixed wing multi engine'), ('6', 'Rotorcraft'), ('7', 'Weight-shift-control'), ('8', 'Powered Parachute'), ('9', 'Gryroplane')], max_length=4)),
                ('status', models.CharField(max_length=4)),
                ('registrant_type', models.CharField(choices=[('1', 'Individual'), ('2', 'Partnership'), ('3', 'Corporation'), ('4', 'Co-Owned'), ('5', 'Government'), ('8', 'Non Citizen Corporation'), ('9', 'Non Citizen Co-Owned')], max_length=4)),
                ('registrant_name', models.TextField()),
                ('registrant_street', models.TextField()),
                ('registrant_street2', models.TextField()),
                ('registrant_city', models.TextField()),
                ('registrant_state', models.TextField()),
                ('registrant_zipcode', models.TextField()),
                ('registrant_region', models.TextField()),
                ('registrant_county', models.TextField()),
                ('registrant_country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AltitudeReport',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('altitude', models.IntegerField()),
                ('aircraft', models.ForeignKey(related_name='altitudes', to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='CallsignReport',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('callsign', models.CharField(max_length=8)),
                ('aircraft', models.ForeignKey(related_name='callsigns', to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='HeadingReport',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('speed', models.IntegerField()),
                ('heading', models.IntegerField()),
                ('aircraft', models.ForeignKey(related_name='headings', to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='LocationReport',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ground', models.BooleanField(db_index=True)),
                ('aircraft', models.ForeignKey(related_name='locations', to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=16)),
                ('manufacturer', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SquawkReport',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=4)),
                ('aircraft', models.ForeignKey(related_name='squawks', to='sigpoll.Aircraft')),
            ],
        ),
        migrations.AddField(
            model_name='aircraft',
            name='model',
            field=models.ForeignKey(to='sigpoll.Model', null=True),
        ),
        migrations.AlterIndexTogether(
            name='squawkreport',
            index_together=set([('when', 'aircraft')]),
        ),
        migrations.AlterIndexTogether(
            name='locationreport',
            index_together=set([('when', 'aircraft'), ('ground', 'aircraft')]),
        ),
        migrations.AlterIndexTogether(
            name='headingreport',
            index_together=set([('when', 'aircraft')]),
        ),
        migrations.AlterIndexTogether(
            name='callsignreport',
            index_together=set([('when', 'aircraft'), ('callsign', 'aircraft'), ('when', 'callsign')]),
        ),
        migrations.AlterIndexTogether(
            name='altitudereport',
            index_together=set([('when', 'aircraft')]),
        ),
    ]
