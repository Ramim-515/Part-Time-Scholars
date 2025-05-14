"""
URL configuration for PTS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobapp import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Public
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),  # custom view you'll need to create
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='myapp/forgot_password.html'), name='password_reset'),

    # Student
    path('myapp/student_profile/', views.student_profile, name='student_profile'),
    path('student/profile/edit/', views.edit_profile, name='edit_profile'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('student/applied-jobs/', views.applied_jobs, name='applied_jobs'),


    # Employer
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('employer/post-job/', views.post_job, name='post_job'),
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('employer/edit-profile/', views.edit_profile, name='edit_profile'),
    path('employer/post-job/', views.post_job, name='post_job'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('job/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('employer/job/<int:job_id>/applicants/', views.job_applicants, name='job_applicants'),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

