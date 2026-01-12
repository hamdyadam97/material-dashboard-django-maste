# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('super', 'Super Admin'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def get_queryset(user, model):
        if user.role == 'super':
            return model.objects.all()
        return model.objects.filter(created_by=user.employee)