# Generated by Django 3.2.8 on 2021-10-18 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0007_auto_20211018_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='assign_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 8, 15, 21, 40244, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='info',
            field=models.CharField(default='Upcoming', max_length=100),
        ),
    ]
