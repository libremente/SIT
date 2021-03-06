# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0017_auto_20190201_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastreDataAccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('user', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('msg', models.TextField()),
            ],
        ),
    ]
