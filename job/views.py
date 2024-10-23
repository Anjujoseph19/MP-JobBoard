from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from company.models import Company
from .form import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import JobFilter

# Create your views here.
User = get_user_model()

#creating Job
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            company = Company.objects.get(pk=request.user.company.pk)
            var.company = company
            var.save()
            messages.success(request,'New job has been created and saved, Please add other requirements')
            return redirect(reverse('job-details', args=[var.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect('create-job')
    else:
        form = CreateJobForm()
        context = {'form':form}
    return render(request,'job/create_job.html', context)

#Updating Job
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request,'Job information has been updated')
            return redirect(reverse('job-details', args=[job.pk])) #job-details
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('update-job', args=[job.pk]))   #company-details
    else:
        form = UpdateJobForm(instance=job)
        context = {'form':form}
    return render(request,'job/update_job.html',context)

def delete_job(request, pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    messages.success(request, 'Job has been deleted from the database.')
    return redirect('jobs-per-company')

def jobs_per_company(request):
    company = Company.objects.get(pk=request.user.company.pk)
    jobs = company.job_set.all()
    context ={'jobs':jobs}
    return render(request, 'job/jobs_per_company.html', context)

def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    company = Company.objects.get(pk=job.company.pk)
    jobs = company.job_set.all()[:3]
    context ={'job':job, 'company':company, 'jobs':jobs}
    return render(request, 'job/job_details.html', context)

def add_jobres(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobRes(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request,'New Job responsibility added to job details')
            return redirect(reverse('add-jobres', args=[job.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('add-jobres', args=[job.pk]))
    else:
        form = AddJobRes()
        context = {'form':form, 'job':job}
    return render(request,'job/add_jobres.html', context)

def add_jobexp(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobExp(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request,'New Job Experience added to Job details!')
            return redirect(reverse('add-jobexp', args=[job.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('add-jobexp', args=[job.pk]))
    else:
        form = AddJobExp()
        context = {'form':form, 'job':job}
    return render(request, 'job/add_jobexp.html', context)

def delete_jobres(request, pk):
    jobres = JobRes.objects.get(pk=pk)
    get_job = jobres.job
    jobres.delete()
    messages.success(request,'Job responsibilty has been deleted from the Job')
    return redirect(reverse('job-details', args=[get_job.pk]))

def delete_jobexp(request, pk):
    jobexp = JobExp.objects.get(pk=pk)
    get_job = jobexp.job
    jobexp.delete()
    messages.success(request,'Job Experience has been deleted from the Job')
    return redirect(reverse('job-details', args=[get_job.pk]))

def available_jobs(request):
    #jobs = JobFilter(request.GET, queryset=Job.objects.filter(status='Pending').order_by('-date_time_posted'))
    jobs = Job.objects.filter(status='Active').order_by('-date_time_posted')
    #pagination
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    try:
        objects = paginator.page(page_number)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    context = {'jobs':objects, 'filter':jobs}
    return render(request,'job/available_job.html', context)

def apply_to_job(request, pk):
    job = Job.objects.get(pk=pk)
    check_application =job.jobapplication_set.filter(job=job, resume=request.user.resume).exists()

    if job.status == 'Active':
        if request.user.has_resume:
            if not check_application:
                JobApplication.objects.create(job=job,resume=request.user.resume)
                messages.success(request,'You have successfully applied to this Job! You can see progress in Dashboard')
                return redirect(reverse('job-details', args=[job.pk]))
            else:
                messages.warning(request,'You have already applied to this Job')
                return redirect(reverse('job-details', args=[job.pk]))
        else:
            messages.warning(request,'You do not have a Resume. Please create one to apply')
            return redirect(reverse('job-details', args=[job.pk]))
    else:
        messages.warning(request,'This Job is no longer active')
        return redirect(reverse('job-details', args=[job.pk]))
    
def save_job(request, pk):
    job = Job.objects.get(pk=pk)
    check_instane =job.savejob_set.filter(job=job, resume=request.user.resume).exists()
    
    if not check_instane:
        SaveJob.objects.create(job=job,resume=request.user.resume)
        messages.success(request,'You just successfully saved this Job')
        return redirect(reverse('job-details', args=[job.pk]))
    else:
        messages.warning(request,'You have already saved this Job')
        return redirect(reverse('job-details', args=[job.pk]))
    
def manage_applied_jobs(request):
    jobs = JobApplication.objects.filter(resume=request.user.resume)
    context = {'jobs':jobs}
    return render(request, 'job/manage_applied_jobs.html', context)

def delete_application(request, pk):
    job_application = JobApplication.objects.get(pk=pk)
    job_application.delete()
    messages.success(request,'You have deleted the job application')
    return redirect('manage-applied-jobs')

def applicants_per_job(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.jobapplication_set.all()
    approved = applicants.filter(status='Accepted')
    rejected = applicants.filter(status='Declined')
    context = {'applicants':applicants, 'job': job, 'approved':approved, 'rejected':rejected}
    return render(request, 'job/applicants_per_job.html', context)

def accept_application(request, pk):
    appliction = JobApplication.objects.get(pk=pk)
    appliction.status = 'Accepted'
    appliction.save()
    messages.success(request,'You have accepted this candidate')
    return redirect(reverse('applicants-per-job', args=[appliction.job.pk]))

def reject_application(request, pk):
    appliction = JobApplication.objects.get(pk=pk)
    appliction.status = 'Declined'
    appliction.save()
    messages.success(request,'You have rejected this candidate')
    return redirect(reverse('applicants-per-job', args=[appliction.job.pk]))

def all_saved_jobs(request):
    jobs = SaveJob.objects.filter(resume=request.user.resume)
    context = {'jobs':jobs}
    return render(request, 'job/all_saved_jobs.html', context)

def delete_saved_job(request, pk):
    job = SaveJob.objects.get(pk=pk)
    job.delete()
    messages.success(request,'Saved job has been removed from your dashboard')
    return redirect('all-saved-jobs')

