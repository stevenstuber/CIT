# Generated by Django 2.2.13 on 2020-08-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0065_censussubdivision_population_count_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='censussubdivision',
            name='households_owner_count_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='households_tenant_count_total',
            field=models.IntegerField(null=True),
        ),
    ]
