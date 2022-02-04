# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-06 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0006_auto_20171004_1143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='particella',
            unique_together=set([('id_particella', 'progressivo', 'codice_comune', 'sezione', 'foglio', 'numero', 'denominatore', 'subalterno')]),
        ),
        migrations.RunSQL(
            "CREATE UNIQUE INDEX particella_id_particella_progressiv_093d31c1_inde ON public.particella "
            "USING btree ("
            "id_particella, "
            "(COALESCE(progressivo, '-1'::integer)), "
            "(COALESCE(codice_comune, '0000'::character varying)) COLLATE pg_catalog.\"default\", "
            "(COALESCE(sezione, '-1'::integer)), "
            "(COALESCE(foglio, 'AAAA'::character varying)) COLLATE pg_catalog.\"default\", "
            "(COALESCE(numero, 'AAAAA'::character varying)) COLLATE pg_catalog.\"default\", "
            "(COALESCE(denominatore, '-1'::integer)), "
            "(COALESCE(subalterno, 'AAAA'::character varying)) COLLATE pg_catalog.\"default\")"
        )
    ]