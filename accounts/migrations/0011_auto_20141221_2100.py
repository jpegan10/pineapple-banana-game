# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20141220_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(default=10000, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default=b'accountname', max_length=30, verbose_name=b'Gambling Team Name'),
        ),
        migrations.AlterField(
            model_name='availableline',
            name='result',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Won', b'Wager Won'), (b'Lost', b'Wager Lost'), (b'Pushed', b'Wager Pushed')]),
        ),
    ]
