from django.db import models

# Create your models here.
# sectors/models.py
from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=100)
    is_military = models.BooleanField(default=False)

    def __str__(self):
        return self.name
