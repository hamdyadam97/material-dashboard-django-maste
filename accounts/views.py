from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import EmployeeCreateForm
from accounts.models import User


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'بيانات الدخول غير صحيحة'
            })

    return render(request, 'accounts/login.html')


@login_required(login_url='accounts:login')
def dashboard_view(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'accounts/dashboard.html', context)




def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST)

        if form.is_valid():
            employee = form.save(commit=False)
            employee.branch = request.user.branch
            employee.save()

            messages.success(request, 'Employee created successfully')
            return redirect('accounts:create_employee')
    else:
        form = EmployeeCreateForm()

    return render(request, 'accounts/create_employee.html', {
        'form': form
    })

