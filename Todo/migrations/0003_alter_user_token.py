# Generated by Django 3.2.8 on 2021-10-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_dashboard_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
    ]