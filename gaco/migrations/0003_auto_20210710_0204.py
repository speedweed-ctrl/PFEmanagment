# Generated by Django 3.2.4 on 2021-07-10 01:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gaco', '0002_auto_20210710_0200'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.RenameModel(
            old_name='shippingAddress',
            new_name='shippingAddres',
        ),
    ]