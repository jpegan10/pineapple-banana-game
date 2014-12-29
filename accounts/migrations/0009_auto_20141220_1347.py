# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20141217_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='cleared',
            new_name='public',
        ),
        migrations.RemoveField(
            model_name='account',
            name='available_balance',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='completed',
        ),
        migrations.AddField(
            model_name='transaction',
            name='forward_balance',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='previous_balance',
            field=models.DecimalField(default='0', max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]
