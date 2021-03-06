# Generated by Django 2.2.3 on 2020-05-21 10:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sNeeds.apps.account.models
import sNeeds.apps.account.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_delete_studentdetailedinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFormApplySemesterYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('semester', models.CharField(choices=[('بهار', 'بهار'), ('تابستان', 'تابستان'), ('پاییز', 'پاییز\u200d'), ('زمستان', 'زمستان')], max_length=64)),
            ],
            options={
                'ordering': ['year', 'semester'],
            },
        ),
        migrations.CreateModel(
            name='StudentFormFieldsChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(help_text='Lowercase pls', unique=True)),
                ('category', models.CharField(choices=[('grade', 'grade'), ('major', 'major'), ('university', 'university'), ('apply_grade', 'apply_grade'), ('apply_major', 'apply_major'), ('apply_country', 'apply_country'), ('apply_mainland', 'apply_mainland'), ('marital_status', 'marital_status'), ('apply_university', 'apply_university'), ('language_certificate', 'language_certificate'), ('degree_conferral_year', 'degree_conferral_year')], max_length=256)),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='StudentDetailedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(100)])),
                ('total_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('thesis_title', models.CharField(blank=True, max_length=512, null=True)),
                ('language_certificate_overall', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('language_speaking', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('language_listening', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('language_writing', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('language_reading', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('comment', models.TextField(blank=True, max_length=1024, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to=sNeeds.apps.account.models.get_student_resume_path, validators=[sNeeds.apps.account.validators.validate_resume_file_extension, sNeeds.apps.account.validators.validate_resume_file_size])),
                ('apply_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_country', to='account.StudentFormFieldsChoice')),
                ('apply_grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_grade', to='account.StudentFormFieldsChoice')),
                ('apply_mainland', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_mainland', to='account.StudentFormFieldsChoice')),
                ('apply_major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_major', to='account.StudentFormFieldsChoice')),
                ('apply_semester_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_semester_year', to='account.StudentFormApplySemesterYear')),
                ('apply_university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apply_university', to='account.StudentFormFieldsChoice')),
                ('degree_conferral_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='degree_conferral_year', to='account.StudentFormFieldsChoice')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grade', to='account.StudentFormFieldsChoice')),
                ('language_certificate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='language_certificate', to='account.StudentFormFieldsChoice')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='major', to='account.StudentFormFieldsChoice')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marital_status', to='account.StudentFormFieldsChoice')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='university', to='account.StudentFormFieldsChoice')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
