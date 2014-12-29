# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_availableline_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='t_type',
            field=models.CharField(default=b'Debit', max_length=6, choices=[(b'Debit', b'Debit Transaction'), (b'Credit', b'Credit Transaction')]),
        ),
    ]
