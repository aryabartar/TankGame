# Generated by Django 2.2.3 on 2019-07-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAuth', '0002_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='phone number'),
        ),
    ]