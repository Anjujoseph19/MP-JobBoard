# Generated by Django 4.2.13 on 2024-10-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_job_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_qualification',
            field=models.CharField(choices=[('Secondary', 'Secondary'), ('Diploma', 'Diploma'), ('Bachelors Degree', 'Bachelors Degree'), ('Masters Degree', 'Masters Degree'), ('PhD', 'PhD'), ('Doctorate', 'Doctorate')], max_length=100, null=True),
        ),
    ]
