# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20141216_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wagerpaid',
            name='wagerwon',
        ),
        migrations.AddField(
            model_name='availableline',
            name='won',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'Gambling Team Name'),
        ),
    ]
