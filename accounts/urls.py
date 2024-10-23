from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('register-candidate/', register_candidate, name='register-candidate'),
    path('register-recruiter/', register_recruiter, name='register-recruiter'),
    path('login/', login_user, name='login'),
    #path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('change-password/', change_password, name='change-password'),
    path('update-profile/<int:pk>/', update_profile, name='update-profile'),
    path('delete-profile/<int:pk>/', delete_profile, name='delete-profile')
]
