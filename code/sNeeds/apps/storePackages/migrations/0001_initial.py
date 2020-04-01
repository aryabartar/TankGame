# Generated by Django 2.2.3 on 2020-03-22 18:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    # initial = True

    dependencies = [
        ('store', '0007_auto_20200322_1810'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultants', '0003_auto_20200309_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldStorePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('paid_price', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('consultant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                 to='consultants.ConsultantProfile')),
                ('sold_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StorePackage',
            fields=[
                ('product_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='store.Product')),
                ('title', models.CharField(max_length=1024)),
                ('total_price', models.PositiveIntegerField(blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            bases=('store.product',),
        ),
        migrations.CreateModel(
            name='StorePackagePhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('detailed_title',
                 models.CharField(help_text='This field is for ourselves, Feel free to add details.', max_length=1024)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='StorePackagePhaseThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('store_package',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storePackages.StorePackage')),
                ('store_package_phase',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storePackages.StorePackagePhase')),
            ],
            options={
                'ordering': ['phase_number'],
                'unique_together': {('store_package', 'phase_number'), ('store_package', 'store_package_phase')},
            },
        ),
        migrations.AddField(
            model_name='storepackage',
            name='store_package_phases',
            field=models.ManyToManyField(related_name='store_packages',
                                         through='storePackages.StorePackagePhaseThrough',
                                         to='storePackages.StorePackagePhase'),
        ),
        migrations.CreateModel(
            name='SoldStoreUnpaidPackagePhase',
            fields=[
                ('soldproduct_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='store.SoldProduct')),
                ('title', models.CharField(max_length=1024)),
                ('detailed_title',
                 models.CharField(help_text='This field is for ourselves, Feel free to add details.', max_length=1024)),
                ('phase_number', models.IntegerField()),
                ('consultant_done', models.BooleanField(default=False)),
                ('status', models.CharField(
                    choices=[('not_started', 'شروع نشده'), ('pay_to_start', 'نیازمند پرداخت برای شروع'),
                             ('in_progress', 'در حال انجام'), ('done', 'انجام شده')], default='not_started',
                    max_length=128)),
                ('sold_store_package',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storePackages.SoldStorePackage')),
            ],
            options={
                'ordering': ['phase_number'],
                'abstract': False,
            },
            bases=('store.soldproduct', models.Model),
        ),
        migrations.CreateModel(
            name='SoldStorePaidPackagePhase',
            fields=[
                ('product_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='store.Product')),
                ('title', models.CharField(max_length=1024)),
                ('detailed_title',
                 models.CharField(help_text='This field is for ourselves, Feel free to add details.', max_length=1024)),
                ('phase_number', models.IntegerField()),
                ('consultant_done', models.BooleanField(default=False)),
                ('status', models.CharField(
                    choices=[('not_started', 'شروع نشده'), ('pay_to_start', 'نیازمند پرداخت برای شروع'),
                             ('in_progress', 'در حال انجام'), ('done', 'انجام شده')], default='not_started',
                    max_length=128)),
                ('sold_store_package',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storePackages.SoldStorePackage')),
            ],
            options={
                'ordering': ['phase_number'],
                'abstract': False,
            },
            bases=('store.product', models.Model),
        ),
    ]
