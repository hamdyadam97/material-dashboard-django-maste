# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from branches.models import Branch


class User(AbstractUser):
    ROLE_CHOICES = (
        ('super', 'Super Admin'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    def get_queryset(user, model):
        if user.role == 'super':
            return model.objects.all()
        return model.objects.filter(created_by=user.employee)