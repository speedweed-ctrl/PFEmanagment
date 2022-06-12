# Generated by Django 3.2.4 on 2021-07-30 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gaco', '0003_auto_20210710_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoostReview',
            fields=[
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('Comment', models.TextField(max_length=500, null=True)),
                ('CreatedAt', models.DateField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Boost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaco.boost')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoachReview',
            fields=[
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('Comment', models.TextField(max_length=500, null=True)),
                ('CreatedAt', models.DateField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaco.coach')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]