# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180208_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptor',
            name='location',
            field=models.CharField(default='Delhi', max_length=200),
        ),
        migrations.AddField(
            model_name='donor',
            name='location',
            field=models.CharField(default='Delhi', max_length=200),
        ),
    ]
