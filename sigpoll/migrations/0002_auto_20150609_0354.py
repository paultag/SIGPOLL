# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigpoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='tail_number',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
