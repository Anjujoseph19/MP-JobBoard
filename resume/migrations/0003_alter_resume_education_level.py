# Generated by Django 4.2.13 on 2024-10-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resume_candidate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education_level',
            field=models.CharField(choices=[('Diploma', 'Diploma'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=100),
        ),
    ]
