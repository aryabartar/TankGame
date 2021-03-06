# Generated by Django 2.2.3 on 2020-03-16 17:01

from django.db import migrations, models
import sNeeds.apps.customForms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=sNeeds.apps.customForms.models.get_bug_image_path)),
                ('comment', models.CharField(max_length=1024)),
                ('email', models.EmailField(blank=True, max_length=128)),
            ],
        ),
    ]
