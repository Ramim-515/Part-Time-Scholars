from django.db import models

class JobType(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not available', 'Not Available'),
    ]

    name = models.CharField(max_length=50)
    salary = models.IntegerField(null=True, blank=True)
    days = models.IntegerField(null=True, blank=True)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    education = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} applied for {self.job.name}"
