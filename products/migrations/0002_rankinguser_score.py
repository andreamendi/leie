# Generated by Django 2.1.3 on 2018-12-01 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankinguser',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
