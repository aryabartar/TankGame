# Generated by Django 2.2.3 on 2020-03-22 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storePackages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldstorepackage',
            name='sold_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]