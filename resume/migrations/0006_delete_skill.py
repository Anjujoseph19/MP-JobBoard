# Generated by Django 4.2.13 on 2024-10-21 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_resume_education_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
    ]