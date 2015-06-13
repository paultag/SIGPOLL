# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outpost', '0001_initial'),
        ('sigpoll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='altitudereport',
            name='outpost',
            field=models.ForeignKey(to='outpost.Outpost', null=True),
        ),
        migrations.AddField(
            model_name='callsignreport',
            name='outpost',
            field=models.ForeignKey(to='outpost.Outpost', null=True),
        ),
        migrations.AddField(
            model_name='headingreport',
            name='outpost',
            field=models.ForeignKey(to='outpost.Outpost', null=True),
        ),
        migrations.AddField(
            model_name='locationreport',
            name='outpost',
            field=models.ForeignKey(to='outpost.Outpost', null=True),
        ),
        migrations.AddField(
            model_name='squawkreport',
            name='outpost',
            field=models.ForeignKey(to='outpost.Outpost', null=True),
        ),
    ]
