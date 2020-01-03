import uuid as uuid
from django.db import models
from employees.models import Employee


class Expense(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=3)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


