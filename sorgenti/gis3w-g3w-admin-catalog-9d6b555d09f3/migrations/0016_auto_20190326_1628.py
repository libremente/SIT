# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-26 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20190221_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='rndt_file_identifier',
        ),
        migrations.AddField(
            model_name='catalog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='rndt_codice_ente',
            field=models.CharField(blank=True, help_text='RNDT: cod-Ente \xe8 un codice interno a discrezionedell\u2019Amministrazione che pu\xf2 essere anche un progressivo;', max_length=128, null=True, verbose_name='RNDT codice ente per identificatore del file'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='inspire_geographical_extent',
            field=models.CharField(blank=True, help_text='inspire_geographical_extent of the service. Space separated values of lon/lat (west south east north)', max_length=255, null=True, verbose_name='inspire_geographical_extent'),
        ),
    ]
