# Generated by Django 3.2.4 on 2021-08-14 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gaco', '0006_auto_20210814_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfe',
            name='createdAt',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
