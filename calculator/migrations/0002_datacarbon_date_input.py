# Generated by Django 4.1 on 2022-10-22 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacarbon',
            name='date_input',
            field=models.DateField(default=datetime.date(2022, 10, 22)),
        ),
    ]
