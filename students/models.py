from django.db import models

# Create your models here.
# students/models.py
from django.db import models
from sectors.models import Sector
from employees.models import Employee

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    identity_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='students'
    )
