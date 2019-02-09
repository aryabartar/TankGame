# Generated by Django 2.1.3 on 2019-02-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklet', '0004_auto_20190209_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklet',
            name='format',
            field=models.CharField(default='PDF', max_length=40),
        ),
        migrations.AddField(
            model_name='booklet',
            name='language',
            field=models.CharField(choices=[('farsi', 'فارسی'), ('english', 'انگلیسی')], default='farsi', max_length=50),
        ),
        migrations.AddField(
            model_name='booklet',
            name='number_of_pages',
            field=models.IntegerField(default=0, help_text='حتما دقیق نوشته شود'),
        ),
    ]