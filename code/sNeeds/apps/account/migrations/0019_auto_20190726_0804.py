# Generated by Django 2.2.3 on 2019-07-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20190726_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='resume',
            field=models.FileField(null=True, upload_to='file/account/consultant_resume'),
        ),
    ]
