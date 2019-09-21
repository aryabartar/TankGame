# Generated by Django 2.2.3 on 2019-08-03 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190722_1300'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0002_auto_20190803_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=1024)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
