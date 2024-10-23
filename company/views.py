from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from accounts.models import User
from .form import *
from .models import Company

# Create your views here.
User = get_user_model()

def add_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            user = User.objects.get(pk=request.user.pk)
            user.has_company = True
            var.save()
            user.save()
            messages.success(request,'Your company information has been added and saved.')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong.')
            return redirect('add-company')
    else:
        form = AddCompanyForm()
        context = {'form':form}
    return render(request,'company/add_company.html', context)

def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request,'Company information has been updated.')
            return redirect(reverse('company-details', args=[company.pk]))
        else:
            messages.warning(request,'Something went wrong.')
            return redirect(reverse('update-company', args=[company.pk]))
    else:
        form = UpdateCompanyForm(instance=company)
        context = {'form':form}
    return render(request,'company/update_company.html', context)

def company_details(request,pk):
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request,'company/company_details.html', context)