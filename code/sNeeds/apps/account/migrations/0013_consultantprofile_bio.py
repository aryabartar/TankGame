# Generated by Django 2.2.3 on 2019-07-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190722_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
