from django.db import models

# Create your models here.
# programs/models.py
from django.db import models

class Program(models.Model):
    PROGRAM_TYPE = (
        ('diploma', 'Diploma'),
        ('course', 'Course'),
    )

    name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPE)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.name
