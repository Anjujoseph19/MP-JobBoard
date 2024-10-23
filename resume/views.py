from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from company.models import Company
from .form import *
from .models import *

# Create your views here.
User = get_user_model()

#creating resume
def add_resume(request):
    if request.method == 'POST':
        form = AddResumeForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            user = User.objects.get(pk=request.user.pk)
            user.has_resume = True
            var.save()
            user.save()
            messages.success(request,'You have just added your Resume')
            return redirect(reverse('resume-details', args=[var.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect('add-resume')
    else:
        form = AddResumeForm()
        context = {'form':form}
    return render(request,'resume/add_resume.html',context)

#Updating resume
def update_resume(request,pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request,'Resume information has been updated!')
            return redirect(reverse('resume-details', args=[resume.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('resume-resume', args=[resume.pk]))
    else:
        form = UpdateResumeForm(instance=resume)
        context = {'form':form}
    return render(request,'resume/update_resume.html', context)

def resume_details(request,pk):
    resume = Resume.objects.get(pk=pk)
    educations = resume.education_set.all().order_by('-end_date')
    works = resume.work_set.all().order_by('-end_year')
    context = {'resume':resume, 'educations':educations, 'works':works}
    return render(request, 'resume/resume_details.html', context)

'''def delete_resume(request,pk):
    resume = Resume.objects.get(pk=pk)
    resume.delete()
    messages.success(request,'Resume has been deleted')
    return redirect('job-per-company')'''

#Adding education
def add_education(request,pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddEducationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.resume = resume
            var.save()
            messages.success(request,'Education has been added to resume')
            return redirect(reverse('resume-details', args=[resume.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('add-education', args=[resume.pk]))
    else:
        form = AddEducationForm()
        context = {'form':form, 'resume':resume}
    return render(request,'resume/add_education.html', context)

#Updating Education details
def update_education(request, pk):
    education = Education.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateEducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request,'Education information has been updated!')
            return redirect(reverse('resume-details', args=[education.resume.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('update-education', args=[education.pk]))
    else:
        form = UpdateEducationForm(instance=education)
        context = {'form':form}
    return render(request,'resume/update_education.html', context)

#deleting education details
def delete_education(request,pk):
    education = Education.objects.get(pk=pk)
    resume = Resume.objects.get(pk=education.resume.pk)
    education.delete()
    messages.success(request,'Education information has been deleted from your resume')
    return redirect(reverse('resume-details', args=[resume.pk]))

#Adding Work
def add_work(request, pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddWorkForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.resume = resume
            var.save()
            messages.success(request,'Work Experience has been added to resume')
            return redirect(reverse('resume-details', args=[resume.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('add-work', args=[resume.pk]))
    else:
        form = AddWorkForm()
        context = {'form':form, 'resume':resume}
    return render(request,'resume/add_work.html', context)

#Updating work details
def update_work(request,pk):
    work = Work.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateWorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request,'Work Experience information has been updated!')
            return redirect(reverse('resume-details', args=[work.resume.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('update-work', args=[work.pk]))
    else:
        form = UpdateWorkForm(instance=work)
        context = {'form':form}
    return render(request,'resume/update_work.html', context)

#deleteing work details
def delete_work(request,pk):
    work = Work.objects.get(pk=pk)
    resume = Resume.objects.get(pk=work.resume.pk)
    work.delete()
    messages.success(request,'Work Experience information has been deleted from your resume')
    return redirect(reverse('resume-details', args=[resume.pk]))

