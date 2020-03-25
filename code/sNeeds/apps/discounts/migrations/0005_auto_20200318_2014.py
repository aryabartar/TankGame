# Generated by Django 2.2.3 on 2020-03-18 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0004_auto_20200314_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='percent',
        ),
        migrations.AddField(
            model_name='discount',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]