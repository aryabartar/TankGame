# Generated by Django 2.2.3 on 2020-03-19 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_consultantdepositinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultantdepositinfo',
            old_name='tracing_code',
            new_name='consultant_deposit_info_id',
        ),
    ]