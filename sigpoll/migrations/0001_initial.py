# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('tail_number', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AltitudeReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('altitude', models.IntegerField()),
                ('when', models.DateTimeField()),
                ('aircraft', models.ForeignKey(to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='CallsignReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('callsign', models.CharField(max_length=8)),
                ('when', models.DateTimeField()),
                ('aircraft', models.ForeignKey(to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='HeadingReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('speed', models.IntegerField()),
                ('heading', models.IntegerField()),
                ('when', models.DateTimeField()),
                ('aircraft', models.ForeignKey(to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='LocationReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ground', models.BooleanField()),
                ('when', models.DateTimeField()),
                ('aircraft', models.ForeignKey(to='sigpoll.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='aircraft',
            name='model',
            field=models.ForeignKey(to='sigpoll.Model', null=True),
        ),
    ]
