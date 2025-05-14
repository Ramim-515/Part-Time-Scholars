from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, StudentProfile, EmployerProfile, Job, Application

# Extend the default UserAdmin to include 'role'
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff')

# Registering models
admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(EmployerProfile)
admin.site.register(Job)
admin.site.register(Application)
