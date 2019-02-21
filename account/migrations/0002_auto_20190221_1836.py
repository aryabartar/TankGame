# Generated by Django 2.1.3 on 2019-02-21 18:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='phone',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(9000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
