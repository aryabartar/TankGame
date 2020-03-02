# Generated by Django 2.2.3 on 2020-02-21 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_time_slot_sales_number_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_slot_sales_number_discount',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]