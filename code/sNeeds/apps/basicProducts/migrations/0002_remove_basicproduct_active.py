# Generated by Django 2.2.3 on 2020-03-22 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicProducts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicproduct',
            name='active',
        ),
    ]
