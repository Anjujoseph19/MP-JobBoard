# Generated by Django 4.2.13 on 2024-10-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_qualification_job_job_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_experience',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
