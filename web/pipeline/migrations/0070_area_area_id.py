# Generated by Django 2.2.13 on 2020-08-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0069_community_is_coastal'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='area_id',
            field=models.IntegerField(help_text='Original ID of data point', null=True),
        ),
    ]