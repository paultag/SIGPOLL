# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigpoll', '0002_auto_20150609_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='registrant_city',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_country',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_county',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_name',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_region',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_state',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_street',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_street2',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_type',
            field=models.CharField(max_length=4, default='1', choices=[('1', 'Individual'), ('2', 'Partnership'), ('3', 'Corporation'), ('4', 'Co-Owned'), ('5', 'Government'), ('8', 'Non Citizen Corporation'), ('9', 'Non Citizen Co-Owned')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='registrant_zipcode',
            field=models.TextField(default='foo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='status',
            field=models.CharField(max_length=4, default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='type',
            field=models.CharField(max_length=4, default='1', choices=[('1', 'Glider'), ('2', 'Balloon'), ('3', 'Blimp/Dirigible'), ('4', 'Fixed wing single engine'), ('5', 'Fixed wing multi engine'), ('6', 'Rotorcraft'), ('7', 'Weight-shift-control'), ('8', 'Powered Parachute'), ('9', 'Gryroplane')]),
            preserve_default=False,
        ),
    ]
