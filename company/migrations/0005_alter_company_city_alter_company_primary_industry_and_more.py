# Generated by Django 4.2.13 on 2024-10-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_primary_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(choices=[('Kochi', 'Kochi'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Teaneck', 'Teaneck'), ('Bengaluru', 'Bengaluru'), ('England', 'England'), ('Dublin', 'Dublin')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='primary_industry',
            field=models.CharField(choices=[('IT', 'IT'), ('Manufacturing', 'Manufacturing'), ('Financial Services', 'Financial Services'), ('Accounting & Taxation', 'Accounting & Taxation'), ('Banking & Lending', 'Banking & Lending'), ('Grocery Stores', 'Grocery Stores'), ('Internet & Web Services', 'Internet & Web Services')], max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(choices=[('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Maharashtra', 'Maharashtra'), ('New Jersey', 'New Jersey'), ('New York City', 'New York City'), ('Chicago', 'Chicago'), ('San Francisco', 'San Francisco'), ('Toronto', 'Toronto'), ('Burlington', 'Burlington'), ('London', 'London')], max_length=100),
        ),
    ]
