# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-10-03 10:01
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0030_auto_20190528_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catasto',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=32633),
        ),
    ]