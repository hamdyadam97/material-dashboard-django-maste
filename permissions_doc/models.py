from django.db import models


from django.db import models
from enrollments.models import Enrollment
from employees.models import Employee

class PermissionDocument(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    issued_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='permissions/')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    issued_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)




