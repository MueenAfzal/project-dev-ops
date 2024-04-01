from django.shortcuts import render,redirect
from .models import EmployeeScheduler
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            # ...

            # Redirect to the index page of the scheduler app
            return redirect('scheduler:index')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def index(request):
    # Fetch employee data from the database
    employees = EmployeeScheduler.objects.all()
    print(employees)

    # Pass the employee data to the template context
    context = {
        'employees': employees
    }
    
    # Render the index.html template with the employee data
    return render(request, 'index.html', context)

def about(request):
    # Your logic for the about page goes here
    return render(request, 'about.html')

def contact(request):
    # Your logic for the contact page goes here
    return render(request, 'contact.html')
