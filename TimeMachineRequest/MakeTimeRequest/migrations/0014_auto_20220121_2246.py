# Generated by Django 3.2 on 2022-01-21 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MakeTimeRequest', '0013_alter_request_time_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='time_request',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 19, 46, tzinfo=utc)),
        ),
    ]
