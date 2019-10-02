# Generated by Django 2.2.3 on 2019-07-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190721_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='soldorder',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('canceled_not_refunded', 'Canceled but not refunded'), ('canceled_refunded', 'Canceled and refunded')], default='paid', max_length=256),
        ),
    ]