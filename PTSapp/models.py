from django.db import models

# Create your models here.

class JobType(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank = True, null= True)

    def __str__(self):
        return self.name

class jobs(models.Model):
    name = models.CharField(max_length=50)
    model_year = models.IntegerField()
    jobtype = models.ForeignKey('JobType', on_delete=models.CASCADE)
    status_choices = (
        ('available', 'available'),
        ('not available', 'not available'),
    )
    status = models.CharField(max_length=30, choices=status_choices)

    def _str_(self):
        return self.name 