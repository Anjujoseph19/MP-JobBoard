from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('available-jobs/', browse_jobs, name='available-jobs'),
    path('recuriters/', recuriters, name='recuriters'),
    path('candidates/', candidates, name='candidates'),
    path('about-us/', about_us, name='about-us'),
    path('contact/', contact, name='contact')
]
