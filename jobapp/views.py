from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .decorator import role_required
from .models import *
from .forms import *

# ----------------- Public Views -----------------

def home(request):
    """Display homepage with recent jobs."""
    jobs = Job.objects.all().order_by('-posted_at')[:5]
    return render(request, 'myapp/home.html', {'jobs': jobs})

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def job_list(request):
    jobs = Job.objects.all()

    location = request.GET.get('location')
    job_type = request.GET.get('job_type')
    min_salary = request.GET.get('min_salary')

    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if min_salary:
        jobs = jobs.filter(salary__gte=min_salary)

    return render(request, 'myapp/jobs.html', {'jobs': jobs})

def job_details(request, job_id):
    """Show detailed view of a job."""
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'myapp/job_details.html', {'job': job})

# ----------------- Registration -----------------

def register(request):
    """Register a new user and auto-login."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')

            # Create profile based on role
            if role == 'student':
                StudentProfile.objects.create(user=user)
            elif role == 'employer':
                EmployerProfile.objects.create(user=user)

            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'myapp/register.html', {'form': form})

# ----------------- Profile Views -----------------

@login_required
def edit_profile(request):
    """Edit student or employer profile."""
    if request.user.role == 'student':
        profile, _ = StudentProfile.objects.get_or_create(user=request.user)
        form_class = StudentProfileForm
        redirect_url = 'student_profile'
    elif request.user.role == 'employer':
        profile, _ = EmployerProfile.objects.get_or_create(user=request.user)
        form_class = EmployerProfileForm
        redirect_url = 'employer_dashboard'
    else:
        messages.error(request, 'Invalid role.')
        return redirect('home')

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect(redirect_url)
    else:
        form = form_class(instance=profile)

    return render(request, 'myapp/edit_profile.html', {'form': form})

# ----------------- Student Views -----------------

@login_required
@role_required('student')
def student_profile(request):
    """Student profile view."""
    profile = getattr(request.user, 'studentprofile', None)
    return render(request, 'myapp/student_profile.html', {'profile': profile})

@login_required
@role_required('student')
def student_dashboard(request):
    """Student dashboard showing applications."""
    applications = Application.objects.filter(student=request.user.studentprofile)
    return render(request, 'myapp/student_dashboard.html', {'applications': applications})

@login_required
@role_required('student')
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        experience = request.POST.get('experience')

        if not cover_letter or not experience:
            messages.error(request, "Both cover letter and experience are required.")
            return redirect('apply_job', job_id=job_id)

        already_applied = Application.objects.filter(student=request.user.studentprofile, job=job).exists()
        if already_applied:
            messages.warning(request, "You have already applied to this job.")
            return redirect('applied_jobs')

        Application.objects.create(
            student=request.user.studentprofile,
            job=job,
            cover_letter=cover_letter,
            experience=experience
        )
        messages.success(request, "Application submitted successfully.")
        return redirect('applied_jobs')

    return render(request, 'myapp/apply_job.html', {'job': job})



@login_required
@role_required('student')
def applied_jobs(request):
    """List of jobs the student has applied to."""
    applications = Application.objects.filter(student=request.user.studentprofile).select_related('job')
    return render(request, 'myapp/applied_jobs.html', {'applications': applications})
# ----------------- Employer Views -----------------

@login_required
@role_required('employer')
def employer_dashboard(request):
    """Employer dashboard showing posted jobs."""
    profile = request.user.employerprofile
    jobs = Job.objects.filter(employer=profile)
    return render(request, 'myapp/employer_dashboard.html', {'employer_profile': profile, 'posted_jobs': jobs})

@login_required
@role_required('employer')
def post_job(request):
    """Post a new job."""
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employerprofile
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('employer_dashboard')
    else:
        form = JobForm()

    return render(request, 'myapp/post_job.html', {'form': form})

@login_required
@role_required('employer')
def edit_job(request, job_id):
    """Edit an existing job."""
    job = get_object_or_404(Job, id=job_id, employer=request.user.employerprofile)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm(instance=job)

    return render(request, 'myapp/edit_job.html', {'form': form, 'job': job})

@login_required
@role_required('employer')
def delete_job(request, job_id):
    """Delete a job."""
    job = get_object_or_404(Job, id=job_id, employer=request.user.employerprofile)
    if request.method == 'POST':
        job.delete()
        return redirect('employer_dashboard')

    return render(request, 'myapp/confirm_delete_job.html', {'job': job})

@login_required
@role_required('employer')
def job_applicants(request, job_id):
    """View applicants for a job."""
    job = get_object_or_404(Job, id=job_id, employer=request.user.employerprofile)
    applications = Application.objects.filter(job=job).select_related('student')
    return render(request, 'myapp/view_applicants.html', {'job': job, 'applications': applications})
