from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Application, User, StudentProfile, EmployerProfile

# User Registration Form
class UserRegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employer', 'Employer'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

# Job Posting Form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'job_type', 'salary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateField()
        }
# Application Form
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
# Optional: Student Profile Edit Form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name','photo', 'phone', 'resume', 'education', 'skills']
        widgets = {
        'name': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
        'education': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        'skills': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        'phone': forms.TextInput(attrs={'class': 'form-control'}),
        'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
# Optional: Employer Profile Edit Form
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ['user']  # ✅ All fields except user
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +880123456789'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
        }