# Generated by Django 2.2.9 on 2020-01-09 14:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0032_planimetrieiniziali_sezione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catasto',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=3003),
        ),
        migrations.AlterField(
            model_name='codicipartita',
            name='tipo',
            field=models.CharField(choices=[('F', 'FAB'), ('T', 'TER')], max_length=1),
        ),
        migrations.AlterField(
            model_name='configimportcxf',
            name='db_schema',
            field=models.CharField(default='public', max_length=255, verbose_name='DB schema'),
        ),
        migrations.AlterField(
            model_name='configimportcxf',
            name='srid',
            field=models.ForeignKey(db_column='srid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.G3WSpatialRefSys'),
        ),
        migrations.AlterField(
            model_name='datiatto',
            name='data_efficacia',
            field=models.DateField(blank=True, null=True, verbose_name='Data di Efficacia conclusiva'),
        ),
        migrations.AlterField(
            model_name='datiatto',
            name='data_registrazione',
            field=models.DateField(blank=True, null=True, verbose_name='Data di registrazione conclusiva'),
        ),
        migrations.AlterField(
            model_name='datimdocfa',
            name='sezione_uiu',
            field=models.ForeignKey(blank=True, db_column='sezione', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastre.SezioniCensuarie'),
        ),
        migrations.AlterField(
            model_name='importcatasto',
            name='file',
            field=models.FileField(upload_to='catasto_files'),
        ),
        migrations.AlterField(
            model_name='importdocfa',
            name='file',
            field=models.FileField(upload_to='docfa_files'),
        ),
        migrations.AlterField(
            model_name='personafisica',
            name='data_nascita',
            field=models.DateField(blank=True, null=True, verbose_name='Data di nascita'),
        ),
        migrations.AlterField(
            model_name='personafisica',
            name='luogo_nascita',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Luogo di nascita'),
        ),
        migrations.AlterField(
            model_name='planimetrieiniziali',
            name='sezione',
            field=models.ForeignKey(blank=True, db_column='sezione', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastre.SezioniCensuarie'),
        ),
        migrations.AlterField(
            model_name='prm',
            name='file',
            field=models.FileField(upload_to='prm_files'),
        ),
        migrations.AlterField(
            model_name='relazioneuiudocfa',
            name='sezione_uiu',
            field=models.ForeignKey(blank=True, db_column='sezione', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastre.SezioniCensuarie'),
        ),
        migrations.AlterField(
            model_name='sezionicensuarie',
            name='tipo',
            field=models.CharField(choices=[('F', 'FAB'), ('T', 'TER')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tipinota',
            name='tipo',
            field=models.CharField(choices=[('F', 'FAB'), ('T', 'TER')], max_length=1),
        ),
        migrations.AlterField(
            model_name='titolarita',
            name='soggetto_riferimento',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Soggetto di riferimento'),
        ),
    ]