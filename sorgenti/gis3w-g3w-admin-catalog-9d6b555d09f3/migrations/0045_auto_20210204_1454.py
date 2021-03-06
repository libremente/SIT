# Generated by Django 2.2.16 on 2021-02-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0044_auto_20210122_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='g3w_project_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='G3W-SUITE project id/pk'),
        ),
        migrations.AddField(
            model_name='record',
            name='g3w_project_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='G3W-SUITE project type'),
        ),
    ]
