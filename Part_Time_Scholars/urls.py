from django.contrib import admin
from django.urls import path
from PTSapp import views as pts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pts_views.home, name='home'),
    path('job/', pts_views.job, name='job'),
    path('jobpostpage/', pts_views.jobpostpage, name='jobpostpage'),
    path('studentinfo/', pts_views.studentinfo, name='studentinfo'),
    path('about/', pts_views.about, name='about'),
    path('contact/', pts_views.contact, name='contact'),
    path('profile/', pts_views.profile, name='profile'),
    path('student/<int:id>/', pts_views.profile, name='student_profile'),


    # Auth Views
    path('login/', pts_views.login_view, name='login'),
    path('register/', pts_views.register_view, name='register'),
    path('logout/', pts_views.logout_view, name='logout'),
]


