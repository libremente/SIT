# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0016_auto_20190201_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitaimmobiliare',
            name='categoria',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
