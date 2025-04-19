from django import forms
from .models import Job, JobType

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'salary', 'days', 'jobtype', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=Job.STATUS_CHOICES)
        }
