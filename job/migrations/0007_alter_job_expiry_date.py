# Generated by Django 4.2.13 on 2024-10-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expiry_date',
            field=models.DateTimeField(null=True),
        ),
    ]
