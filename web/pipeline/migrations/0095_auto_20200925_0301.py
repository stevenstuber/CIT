# Generated by Django 2.2.13 on 2020-09-25 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0094_auto_20200925_0253'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dataset',
            new_name='DataSource',
        ),
    ]
