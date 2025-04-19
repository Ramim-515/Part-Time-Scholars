from django.shortcuts import render
from .models import *

def home(request):
    jobs_list = Job.objects.filter(status='available')
    context = {
        'jobs': jobs_list
    }
    return render(request, 'myapp/home.html', context)

def job(request):
    job_types = JobType.objects.all()
    jobs_list = Job.objects.all()
    context = {
        'job_types': job_types,
        'jobs': jobs_list
    }
    return render(request, 'myapp/job.html', context)

from django.shortcuts import render, redirect
from .models import *
from .forms import JobPostForm

def jobpostpage(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobPostForm()
    
    context = {
        'form': form
    }
    return render(request, 'myapp/jobpostpage.html', context)


def studentinfo(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'myapp/studentinfo.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def profile(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'myapp/profile.html', context)
