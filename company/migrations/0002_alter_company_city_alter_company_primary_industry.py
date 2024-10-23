# Generated by Django 4.2.13 on 2024-10-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(choices=[('Kochi', 'Kochi'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Gurgaon', 'Gurgaon'), ('Bengaluru', 'Bengaluru'), ('England', 'England'), ('Dublin', 'Dublin')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='primary_industry',
            field=models.CharField(choices=[('IT', 'IT'), ('Manufacturing', 'Manufacturing'), ('Banking & Lending', 'Banking & Lending'), ('Accounting & Taxation', 'Accounting & Taxation'), ('Education', 'Education'), ('Grocery Stores', 'Grocery Stores'), ('Internet & Web Services', 'Internet & Web Services')], max_length=100),
        ),
    ]