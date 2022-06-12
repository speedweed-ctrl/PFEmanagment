# Generated by Django 3.2.4 on 2021-07-10 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('title', models.CharField(max_length=50, null=True)),
                ('disciption', models.TextField(max_length=500, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('prices', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('paymentMethod', models.CharField(blank=True, max_length=50, null=True)),
                ('taxPrice', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=5, max_digits=7, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('paidAt', models.DateField(blank=True, null=True)),
                ('deliveredAt', models.DateField(blank=True, null=True)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='shippingAddress',
            fields=[
                ('DiscordAccount', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=60)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaco.order')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
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
            name='orderItem',
            fields=[
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Boost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaco.boost')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaco.order')),
            ],
        ),
    ]
