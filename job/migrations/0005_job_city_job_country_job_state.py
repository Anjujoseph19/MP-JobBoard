# Generated by Django 4.2.13 on 2024-10-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_alter_job_job_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(choices=[('Kochi', 'Kochi'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Gurgaon', 'Gurgaon'), ('Bengaluru', 'Bengaluru'), ('England', 'England'), ('Dublin', 'Dublin')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('Canada', 'Canada')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='state',
            field=models.CharField(choices=[('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Maharashtra', 'Maharashtra'), ('New York City', 'New York City'), ('Chicago', 'Chicago'), ('San Francisco', 'San Francisco'), ('Toronto', 'Toronto'), ('Burlington', 'Burlington'), ('London', 'London')], max_length=100, null=True),
        ),
    ]
