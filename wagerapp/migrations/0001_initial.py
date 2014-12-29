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
            name='AvailableLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.CharField(max_length=120)),
                ('spread', models.FloatField(default=0)),
                ('pays', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bettor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', models.FloatField(null=True, blank=True)),
                ('projected', models.FloatField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
                ('home_team', models.CharField(max_length=120)),
                ('away_team', models.CharField(max_length=120)),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('tied', models.BooleanField(default=False)),
                ('home_win', models.NullBooleanField()),
                ('home_margin', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('wageramount', models.FloatField()),
                ('won', models.BooleanField(default=False)),
                ('pushed', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('bettor', models.ForeignKey(to='wagerapp.Bettor')),
                ('line', models.ForeignKey(to='wagerapp.AvailableLine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='availableline',
            name='game',
            field=models.ForeignKey(to='wagerapp.Game'),
            preserve_default=True,
        ),
    ]
