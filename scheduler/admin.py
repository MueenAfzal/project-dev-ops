from django.contrib import admin
from .models import User, EmployeeScheduler, Employee

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'employer_id')

@admin.register(EmployeeScheduler)
class EmployeeSchedulerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department', 'start_date', 'end_date', 'comments', 'user')

admin.site.register(Employee)
