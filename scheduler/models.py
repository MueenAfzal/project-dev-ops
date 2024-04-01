from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    employer_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name  # Return a string representation of the object
    
class EmployeeScheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    start_date = models.DateField()  # Add start date field
    end_date = models.DateField()    # Add end date field
    comments = models.TextField()    # Add comments field

    def __str__(self):
        return self.name  # Return a string representation of the object
# models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='employee_profiles/')
    shift_start_time = models.TimeField()

    def __str__(self):
        return self.name
