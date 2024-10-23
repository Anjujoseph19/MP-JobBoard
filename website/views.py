from django.shortcuts import render
from job.models import Job
from company.models import Company
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from .filter import JobFilter

# Create your views here.
def home(request):
    companies = Company.objects.all()
    filter = JobFilter(request.GET, queryset=Job.objects.filter(status='Active').order_by('?'))
    jobs = Job.objects.order_by('?')[:3]    #does not work for larger DB.Only small ones :)
    #jobs = Job.objects.filter(status='Active')[:4]
    context = {'filter':filter, 'jobs':jobs,'companies': companies}
    return render(request,'website/home.html', context)

def browse_jobs(request):
    return render(request,'job/available_job.html')

def about_us(request):
    return render(request,'website/about_us.html')

def contact(request):
    return render(request,'website/contact.html')

def candidates(request):
    applicants = Job.objects.all()
    context = {'applicants': applicants}
    return render(request,'website/candidates.html', context)

def recuriters(request):
    companies = Company.objects.all() 
    context = {'companies': companies}
    return render(request,'website/recuriters.html', context)

# @login_required  # Only logged-in users can access this view
def contact(request):
    user_email = request.user.email  # Get the logged-in user's email
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  # This will already be filled with the user's email
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            email_subject = f"New Contact Form Submission: {subject}"
            email_message = f"You have received a contactform: \nName: {name}\nEmail: {email} \n\nMessage:\n{message}"

            try:
                # Send the email
                send_mail(
                    email_subject,  # Subject
                    email_message,  # Message
                    email,          # From user (their email)
                    ['anjulibin1822@gmail.com'],  # Admin email (your email)
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully. Thank you for contacting us.")
                return redirect('contact')
            except Exception as e:
                messages.error(request, "An error occurred while sending the message. Please try again.")
        else:
            messages.error(request, "Please fill in all the fields.")
    
    return render(request, 'website/contact.html', {'user_email': user_email})
