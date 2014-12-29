# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20141220_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableline',
            name='won',
        ),
        migrations.AddField(
            model_name='availableline',
            name='paidout',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='availableline',
            name='result',
            field=models.CharField(max_length=20, null=True, choices=[(b'Won', b'Wager Won'), (b'Lost', b'Wager Lost'), (b'Pushed', b'Wager Pushed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='availableline',
            name='pays',
            field=models.DecimalField(default=1.909, max_digits=12, decimal_places=3),
        ),
    ]
