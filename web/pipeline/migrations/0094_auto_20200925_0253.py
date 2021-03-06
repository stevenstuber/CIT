# Generated by Django 2.2.13 on 2020-09-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0093_auto_20200925_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='csv_path',
            new_name='source_file_path',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='source_type',
            field=models.CharField(choices=[('csv', 'CSV'), ('api', 'DATABC'), ('shp', 'SHP')], max_length=127, null=True),
        ),
    ]
