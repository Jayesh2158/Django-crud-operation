# Generated by Django 3.2.8 on 2021-10-18 07:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_auto_20211018_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='assign_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 7, 24, 14, 682372, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 7, 24, 14, 682372, tzinfo=utc)),
        ),
    ]