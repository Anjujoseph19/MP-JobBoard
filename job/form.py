from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'date_time_posted', 'date_posted', 'is_published','expiry_date','status')

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'date_time_posted', 'date_posted', 'is_published','expiry_date')

class AddJobRes(forms.ModelForm):
    class Meta:
        model = JobRes
        fields = ['name']

class AddJobExp(forms.ModelForm):
    class Meta:
        model = JobExp
        fields = ['name']
