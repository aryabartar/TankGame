# Generated by Django 2.1.3 on 2019-03-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklet', '0030_auto_20190304_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklet',
            name='booklet_content',
            field=models.URLField(max_length=300),
        ),
    ]
