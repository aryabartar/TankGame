# Generated by Django 2.2.3 on 2019-08-02 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_discount_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='discount_percent',
        ),
    ]