# Generated by Django 2.1.3 on 2019-03-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190310_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='public_classes',
            field=models.ManyToManyField(blank=True, null=True, to='blog.PostLike'),
        ),
    ]