from django.urls import path
from .views import *


urlpatterns = [
    path('create-job/', create_job, name='create-job'),
    path('update-job/<int:pk>/', update_job, name='update-job'),
    path('delete-job/<int:pk>/', delete_job, name='delete-job'),

    path('jobs-per-company/', jobs_per_company, name='jobs-per-company'),
    path('job-details/<int:pk>/', job_details, name='job-details'),

    path('add-jobres/<int:pk>/', add_jobres, name='add-jobres'),
    path('delete-jobres/<int:pk>/', delete_jobres, name='delete-jobres'),
    
    path('add-jobexp/<int:pk>/', add_jobexp, name='add-jobexp'),
    path('delete-jobexp/<int:pk>/', delete_jobexp, name='delete-jobexp'),

    path('available-jobs/', available_jobs, name='available-jobs'),
    path('apply-to-job/<int:pk>/', apply_to_job, name='apply-to-job'),
    path('save-job/<int:pk>/', save_job, name='save-job'),
    path('manage-applied-jobs/', manage_applied_jobs, name='manage-applied-jobs'),
    path('delete-application/<int:pk>/', delete_application, name='delete-application'),
    path('applicants-per-job/<int:pk>/', applicants_per_job, name='applicants-per-job'),
    path('accept-application/<int:pk>/', accept_application, name='accept-application'),
    path('reject-application/<int:pk>/', reject_application, name='reject-application'),
    path('all-saved-jobs',all_saved_jobs,name='all-saved-jobs'),
    path('delete-saved-job/<int:pk>/',delete_saved_job,name='delete-saved-job')
]
