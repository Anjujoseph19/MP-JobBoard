# Generated by Django 4.2.13 on 2024-10-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_delete_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skill_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
