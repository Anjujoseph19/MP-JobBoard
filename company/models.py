from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
User = get_user_model()

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cmp_name = models.CharField(max_length=100)
    cmp_ceo = models.CharField(max_length=100)
    cmp_image = models.FileField(null=True,blank=True)
    #cmp_image = models.FileField(upload_to="company_img",null=True,blank=True)
    city = models.CharField(max_length=100, null=True,
                             choices=(('Kochi', 'Kochi'),('Thiruvananthapuram', 'Thiruvananthapuram'),('Pune','Pune'),('Mumbai','Mumbai'),('Teaneck', 'Teaneck'),('Bengaluru','Bengaluru'),('England','England'),('Dublin','Dublin')))
    state = models.CharField(max_length=100,
                             choices=(('Karnataka', 'Karnataka'),('Kerala','Kerala'),('Maharashtra','Maharashtra'),('New Jersey','New Jersey'),
                                      ('New York City','New York City'),('Chicago', 'Chicago'),('San Francisco','San Francisco'),
                                      ('Toronto','Toronto'),('Burlington','Burlington'),('London', 'London')))
    country = models.CharField(max_length=100,
                             choices=(('India', 'India'),('USA','USA'),('Canada','Canada')))
    primary_industry = models.CharField(max_length=100,
                             choices=(('IT', 'IT'),('Manufacturing','Manufacturing'),('Financial Services','Financial Services'),('Accounting & Taxation','Accounting & Taxation'),('Banking & Lending','Banking & Lending'),('Grocery Stores','Grocery Stores'),('Internet & Web Services','Internet & Web Services')))
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255)
    cmp_size = models.CharField(max_length=20,
                                    choices=(('more than 10,000','more than 10,000'),('1,001 to 5,000','1,001 to 5,000'),('500 to 1,000','500 to 1,000'),('70-200','70-200'),('50-100','50-100'),('10-25','10-25')))
    founded_in = models.PositiveIntegerField()
    facebook = models.URLField()
    linked_in = models.URLField()
    twitter= models.URLField()
    website = models.URLField()
    about_company = models.TextField()
