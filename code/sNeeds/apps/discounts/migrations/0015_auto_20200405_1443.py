# Generated by Django 2.2.3 on 2020-04-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0014_auto_20200401_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='creator',
            field=models.CharField(choices=[('consultant', 'Consultant'), ('admin', 'Admin')], default='admin', max_length=10),
        ),
    ]
