# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-10 06:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0028_auto_20190408_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catasto',
            name='data_fin',
        ),
        migrations.RemoveField(
            model_name='catasto',
            name='data_ini',
        ),
    ]
