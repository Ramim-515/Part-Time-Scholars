
from django.urls import path, include

urlpatterns = [
    
    path('', include('jobs.urls')),  # Include your app's URL config
]
