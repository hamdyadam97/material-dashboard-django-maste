from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login



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



def is_admin(user):
    return user.is_superuser
@login_required(login_url='accounts:login')
def user_list(request):
    users = User.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        instance = User.objects.filter(id=user_id).first()
        form = UserForm(request.POST, instance=instance)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('accounts:user_list')
    else:
        form = UserForm()

    return render(request, 'accounts/user_list.html', {
        'users': users,
        'form': form,
    })


