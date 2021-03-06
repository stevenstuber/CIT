# Generated by Django 2.2.13 on 2020-07-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0022_auto_20200711_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('name', 'location_type')},
        ),
    ]
