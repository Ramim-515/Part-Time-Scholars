from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):

    j_s = jobs.objects.all()
    context = {
        'j_s' : j_s
    }
    return render(request, template_name='myapp/home.html')

def job(request):
    Job_Type = JobType.objects.all()
    context = {
        'job_type' : Job_Type
            }
    return render(request, template_name='myapp/job.html')

def jobpostpage(request):
    return render(request, template_name='myapp/jobpostpage.html')

def studentinfo(request):
    return render(request, template_name='myapp/studentinfo.html')

def about(request):
    return render(request, template_name='myapp/about.html')

def contact(request):
    return render(request, template_name='myapp/contact.html')

def profile(request):
    return render(request, template_name='myapp/profile.html')
