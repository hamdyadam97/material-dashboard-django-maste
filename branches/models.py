from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=150, unique=True)
    address = models.TextField()
    establishment_date = models.DateField(null=True, blank=True)

    facilities = models.TextField(
        help_text="المميزات / الإمكانيات المتوفرة في الفرع",
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
