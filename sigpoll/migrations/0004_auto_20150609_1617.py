# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigpoll', '0003_auto_20150609_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquawkReport',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('when', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='names',
        ),
        migrations.AddField(
            model_name='squawkreport',
            name='aircraft',
            field=models.ForeignKey(to='sigpoll.Aircraft'),
        ),
    ]
