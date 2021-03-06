# Generated by Django 2.2.3 on 2020-06-20 18:11

from django.db import migrations, models
import sNeeds.apps.storePackages.models


class Migration(migrations.Migration):

    dependencies = [
        ('storePackages', '0012_storepackage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldstorepackage',
            name='image',
            field=models.ImageField(null=True, upload_to=sNeeds.apps.storePackages.models.get_sold_store_package_image_upload_path),
        ),
        migrations.AlterField(
            model_name='storepackage',
            name='image',
            field=models.ImageField(null=True, upload_to=sNeeds.apps.storePackages.models.get_sold_store_package_image_upload_path),
        ),
    ]
