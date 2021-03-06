# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerDef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('rollback', models.BooleanField()),
                ('dedicated', models.BooleanField()),
                ('update_time', models.TimeField()),
                ('gameid', models.CharField(max_length=1024)),
                ('clients_max', models.IntegerField()),
                ('proto_min', models.IntegerField()),
                ('mapgen', models.CharField(max_length=128)),
                ('updates', models.IntegerField()),
                ('description', models.TextField()),
                ('ping', models.FloatField()),
                ('damage', models.BooleanField()),
                ('password', models.BooleanField()),
                ('uptime', models.IntegerField()),
                ('address', models.CharField(max_length=2048)),
                ('proto_max', models.IntegerField()),
                ('game_time', models.TimeField()),
                ('mods', models.TextField()),
                ('total_clients', models.IntegerField()),
                ('clients', models.IntegerField()),
                ('version', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('pop_v', models.FloatField()),
                ('ip', models.GenericIPAddressField()),
                ('creative', models.BooleanField()),
                ('start', models.TimeField()),
                ('pvp', models.BooleanField()),
                ('lag', models.FloatField()),
                ('can_see_far_names', models.BooleanField()),
                ('port', models.IntegerField()),
                ('clients_top', models.IntegerField()),
                ('privs', models.TextField()),
            ],
        ),
    ]
