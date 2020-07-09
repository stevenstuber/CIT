# Generated by Django 2.2.13 on 2020-07-09 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0014_auto_20200709_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticFacility',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pipeline.Location')),
            ],
            bases=('pipeline.location',),
        ),
    ]