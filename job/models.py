from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company
from resume.models import Resume

# Create your models here.
User = get_user_model()

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_time_posted = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now=True)
    pay = models.PositiveIntegerField()
    pay_mode =models.CharField(max_length=100,
                             choices=(('Daily', 'Daily'),('Weekly','Weekly'),('Monthly','Monthly'),('Yearly','Yearly')))
    work_type = models.CharField(max_length=100,
                             choices=(('Full Time', 'Full Time'),('Part Time','Part Time'),('Fresher','Fresher'),('Intern','Intern'),('Contract','Contract')))
   
    job_location = models.CharField(max_length=20,choices=(('Remote','Remote'),('Hybrid','Hybrid'),('On-site','On-site')))
    expiry_date = models.DateTimeField(null=True)
    hours_per_week = models.PositiveIntegerField()
    job_vacancy = models.CharField(max_length=100,null=True)
    job_experience = models.CharField(max_length=100,null=True)
    job_qualification = models.CharField(max_length=100, null=True, choices=(('Secondary','Secondary'),('Diploma','Diploma'),('Bachelors Degree','Bachelors Degree'),('Masters Degree','Masters Degree'),('PhD','PhD'),('Doctorate','Doctorate')))
    city = models.CharField(max_length=100, null=True,
                             choices=(('Kochi', 'Kochi'),('Thiruvananthapuram', 'Thiruvananthapuram'),('Pune','Pune'),('Mumbai','Mumbai'),('Gurgaon', 'Gurgaon'),('Bengaluru','Bengaluru'),('England','England'),('Dublin','Dublin')))
    state = models.CharField(max_length=100, null=True,
                             choices=(('Karnataka', 'Karnataka'),('Kerala','Kerala'),('Maharashtra','Maharashtra'),
                                      ('New York City','New York City'),('Chicago', 'Chicago'),('San Francisco','San Francisco'),
                                      ('Toronto','Toronto'),('Burlington','Burlington'),('London', 'London')))
    country = models.CharField(max_length=100, null=True,
                             choices=(('India', 'India'),('USA','USA'),('Canada','Canada')))
    job_description = models.TextField()
    is_published = models.BooleanField(default=False)
    status = models.CharField(max_length=40,choices=(('Pending','Pending'),('Active','Active'),('Expired','Expired')),default='Pending')

#Job responsibility
class JobRes(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

#Job experience
class JobExp(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

class JobApplication(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    date_time_applied = models.DateTimeField(auto_now_add=True)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,
                              choices=(('Pending','Pending'),('Accepted','Accepted'),('Declined','Declined')),default='Pending')

class SaveJob(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    date_time_saved = models.DateTimeField(auto_now_add=True)
    date_saved = models.DateField(auto_now_add=True)


