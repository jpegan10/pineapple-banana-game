# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_availableline_won'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='home_margin',
        ),
        migrations.AddField(
            model_name='game',
            name='away_score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
