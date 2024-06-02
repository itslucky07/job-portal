# Generated by Django 5.0 on 2024-03-23 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_recruiteruser_company_recruiteruser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('discription', models.CharField(max_length=300)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=110)),
                ('skills', models.CharField(max_length=110)),
                ('creationdate', models.DateField()),
                ('recruiter_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.recruiteruser')),
            ],
        ),
    ]
