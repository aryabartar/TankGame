# Generated by Django 2.2.3 on 2020-02-21 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200221_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='used_discount',
            new_name='used_consultant_discount',
        ),
    ]
