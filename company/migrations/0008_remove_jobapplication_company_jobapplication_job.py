# Generated by Django 4.1.2 on 2023-03-19 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='company',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.jobpost'),
        ),
    ]