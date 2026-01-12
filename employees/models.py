from django.db import models

# Create your models here.
# employees/models.py
from django.db import models
from accounts.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
