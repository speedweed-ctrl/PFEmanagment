# Generated by Django 3.2.4 on 2021-08-14 22:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gaco', '0010_alter_pfe_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfe',
            name='createdAt',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 14, 22, 28, 33, 758649, tzinfo=utc)),
        ),
    ]
