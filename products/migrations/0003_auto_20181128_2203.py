# Generated by Django 2.1.3 on 2018-11-29 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20181128_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='rents',
            field=models.ManyToManyField(related_name='rents', through='products.Rent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rent',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
