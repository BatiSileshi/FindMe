# Generated by Django 4.1.2 on 2023-01-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_looking_for_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='looking_for_employee',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='looking_for_work',
        ),
        migrations.AddField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(choices=[('work', 'Work'), ('employee', 'Employee')], max_length=20, null=True),
        ),
    ]