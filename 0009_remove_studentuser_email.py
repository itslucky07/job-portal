# Generated by Django 5.0 on 2024-03-25 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0008_studentuser_email_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='email',
        ),
    ]
