# Generated by Django 2.0.2 on 2018-03-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logdatamonit',
            name='dbTrafficText',
            field=models.CharField(default='', max_length=500),
        ),
    ]
