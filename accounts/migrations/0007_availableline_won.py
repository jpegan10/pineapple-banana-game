# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20141217_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableline',
            name='won',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
