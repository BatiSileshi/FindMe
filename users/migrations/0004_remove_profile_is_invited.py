# Generated by Django 4.1.2 on 2023-01-20 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_looking_for_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_invited',
        ),
    ]