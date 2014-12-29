# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('balance', models.DecimalField(max_digits=12, decimal_places=2)),
                ('available_balance', models.DecimalField(max_digits=12, decimal_places=2)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('holder', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvailableLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spread', models.DecimalField(default=0, max_digits=12, decimal_places=1)),
                ('pays', models.DecimalField(default=1, max_digits=12, decimal_places=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gametime', models.DateTimeField()),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('home_margin', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cleared', models.BooleanField(default=False)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('t_type', models.CharField(max_length=6, choices=[(b'Debit', b'Debit Transaction'), (b'Credit', b'Credit Transaction')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WagerMade',
            fields=[
                ('transaction_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.Transaction')),
                ('line', models.ForeignKey(to='accounts.AvailableLine')),
            ],
            options={
            },
            bases=('accounts.transaction',),
        ),
        migrations.CreateModel(
            name='WagerPaid',
            fields=[
                ('transaction_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.Transaction')),
                ('wagerwon', models.NullBooleanField()),
                ('wager', models.ForeignKey(to='accounts.WagerMade')),
            ],
            options={
            },
            bases=('accounts.transaction',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(to='accounts.Account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(related_name=b'away_team', to='accounts.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name=b'home_team', to='accounts.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='availableline',
            name='game',
            field=models.ForeignKey(to='accounts.Game'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='availableline',
            name='team',
            field=models.ForeignKey(to='accounts.Team'),
            preserve_default=True,
        ),
    ]
