# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20141217_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableline',
            name='won',
        ),
        migrations.AddField(
            model_name='wagerpaid',
            name='won',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
