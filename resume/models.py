from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    candidate_image = models.FileField(null=True,blank=True)
    state = models.CharField(max_length=100,
                             choices=(('Karnataka', 'Karnataka'),('Kerala','Kerala'),('Maharashtra','Maharashtra'),
                                      ('New York City','New York City'),('Chicago', 'Chicago'),('San Francisco','San Francisco'),
                                      ('Toronto','Toronto'),('Burlington','Burlington'),('London', 'London')))
    country = models.CharField(max_length=100,
                             choices=(('India', 'India'),('USA','USA'),('Canada','Canada')))
    experience = models.CharField(max_length=100,choices=(('0 - 2', '0 - 2'),('3 - 10', '3 - 10'),('11 - 40', '11 - 40')))
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=30,choices=(('Male','Male'),('Female','Female')))
    language =models.CharField(max_length=100,choices=(('English','English'),('Hindi','Hindi')),default='English')
    education_level = models.CharField(max_length=100,choices=(('Secondary','Secondary'),('Diploma','Diploma'),('Bachelors Degree','Bachelors Degree'),('Masters Degree','Masters Degree'),('PhD','PhD'),('Doctorate','Doctorate')))
    linked_in = models.URLField()
    twitter = models.URLField()
    skill_name = models.CharField(max_length=100, null=True)
    about_candidate = models.TextField()
    phone_number= models.CharField(max_length=20,null=True)

class Education(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    degree_type = models.CharField(max_length=100,choices=(('Bachelors','Bachelors'),('Masters','Masters'),('PhD','PhD')))
    course = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255,null=True)
    start_date = models.PositiveIntegerField()
    end_date = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    still_schooling_here = models.CharField(max_length=100,choices=(('No','No'),('Yes','Yes')),default='No')

class Work(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    role = models.CharField(max_length=100,null=True)
    employment_type = models.CharField(max_length=100, null=True,choices=(('Full-Time','Full-Time'),('Part-Time','Part-Time'),('Self-employed','Self-employed'),('Freelance','Freelance'),('Internship','Internship'),('Trainee','Trainee')))
    company_name = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True,choices=(('Karnataka', 'Karnataka'),('Kerala','Kerala'),('Maharashtra','Maharashtra'),
                                     ('New York City','New York City'),('Chicago', 'Chicago'),('San Francisco','San Francisco'),
                                      ('Toronto','Toronto'),('Burlington','Burlington'),('London', 'London')))
    country = models.CharField(max_length=100,null=True,choices=(('India', 'India'),('USA','USA'),('Canada','Canada')))
    location_type = models.CharField(max_length=255,null=True,choices=(('On-site', 'On-site'),('Hybrid','Hybrid'),('Remote','Remote')))
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.CharField(max_length=1500)
    still_working_here = models.CharField(max_length=100,choices=(('No','No'),('Yes','Yes')),default='No')



