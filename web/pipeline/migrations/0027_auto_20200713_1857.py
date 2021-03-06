# Generated by Django 2.2.13 on 2020-07-13 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0026_area_location_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsunamizone',
            name='zone_class',
            field=models.CharField(help_text='See https://www2.gov.bc.ca/gov/content/safety/emergency-preparedness-response-recovery/preparedbc/know-your-hazards/tsunamis - A-C:moderate D,E:low', max_length=1),
        ),
        migrations.AlterField(
            model_name='wildfirezone',
            name='risk_class',
            field=models.CharField(help_text='A class value signifying the communities WUI Risk Class rating between 1 (low) and 5 (extreme).', max_length=1),
        ),
        migrations.CreateModel(
            name='LocationDistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(blank=True, decimal_places=4, help_text='Driving distance from community to Location', max_digits=24, null=True)),
                ('travel_time', models.IntegerField(blank=True, help_text='Travel time (in minutes) corresponding to driving distance', null=True)),
                ('travel_time_display', models.CharField(blank=True, help_text='Travel time, in human-readable units (e.g. 15 minutes 22 seconds)', max_length=255, null=True)),
                ('driving_route_available', models.BooleanField(blank=True, null=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='distances', to='pipeline.Community')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='distances', to='pipeline.Location')),
            ],
            options={
                'verbose_name': 'Location Distance',
                'verbose_name_plural': 'Location Distances',
                'unique_together': {('community', 'location')},
            },
        ),
    ]
