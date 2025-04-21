from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import JobPostForm, RegisterForm

# ------------------- Public Views -------------------

def home(request):
    jobs_list = Job.objects.filter(status='available')
    return render(request, 'myapp/home.html', {'jobs': jobs_list})

def job(request):
    job_types = JobType.objects.all()
    jobs_list = Job.objects.all()
    return render(request, 'myapp/job.html', {
        'job_types': job_types,
        'jobs': jobs_list
    })

def jobpostpage(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobPostForm()
    return render(request, 'myapp/jobpostpage.html', {'form': form})

def studentinfo(request):
    students = Student.objects.all()
    return render(request, 'myapp/studentinfo.html', {'students': students})

def student_profile(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'myapp/student_profile.html', {'student': student})

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

# ------------------- Authenticated Views -------------------

@login_required
def profile(request):
    students = Student.objects.all()
    return render(request, 'myapp/profile.html', {'students': students})

# ------------------- Authentication Views -------------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
