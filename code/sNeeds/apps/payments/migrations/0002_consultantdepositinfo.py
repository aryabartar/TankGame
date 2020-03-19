# Generated by Django 2.2.3 on 2020-03-19 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0003_auto_20200309_1356'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantDepositInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracing_code', models.CharField(blank=True, help_text='Leave this field blank, this will populate automatically.', max_length=12, unique=True)),
                ('amount', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consultants.ConsultantProfile')),
            ],
        ),
    ]
