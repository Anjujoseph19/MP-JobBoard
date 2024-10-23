from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import *
from .models import User

# Create your views here.
User = get_user_model()

#Candidate Registration_form
def register_candidate(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_candidate = True
            var.username = var.email
            var.save()
            messages.success(request,'Your account has been created. Please login')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-candidate')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request,'accounts/register_candidate.html', context)

#Recruiter Registration_form
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(form)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            messages.success(request,'Your account has been created. Please login')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request,'accounts/register_recruiter.html', context)

#Login_form
def login_user(request):
    next = ''
    
    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            if next == '':
                messages.success(request,"Logged in Successfully.")
                return redirect('dashboard')
            else:
                return redirect(next)
        else:
            messages.warning(request,"Invalid Username or Password!")
            return redirect('login')
    return render(request, 'accounts/login.html')

#Change_password
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-candidate')
    else:
        form = UserPasswordChangeForm(request.user)
        context = {'form':form}
    return render(request,'accounts/change_password.html',context)

#Update_profile
def update_profile(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your information is now updated!')
            return redirect(reverse('update-profile', args=[user.pk]))
        else:
            messages.warning(request,'Something went wrong')
            return redirect(reverse('update-profile', args=[user.pk]))
    else:
        form = UpdateProfileForm(instance=user)
        context = {'form':form}
    return render(request,'accounts/update_profile.html',context)

#deleteing profile
def delete_profile(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request,'The profile has been deleted from JobBoard.')
    return redirect('login')

#logout a user
def logout_user(request):
    logout(request)  
    messages.info(request, 'Your session has ended.')
    return redirect('login')
