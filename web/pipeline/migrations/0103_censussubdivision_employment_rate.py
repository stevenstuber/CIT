# Generated by Django 2.2.13 on 2020-10-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0102_auto_20201015_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='censussubdivision',
            name='employment_rate',
            field=models.FloatField(null=True),
        ),
    ]