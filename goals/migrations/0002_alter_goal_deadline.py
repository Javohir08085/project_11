# Generated by Django 4.2.5 on 2023-09-25 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='deadline',
            field=models.DateField(default=datetime.date(2023, 9, 25)),
        ),
    ]