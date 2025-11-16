from django.db import models
from employees.models import Employee

class Restaurant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='restaurants')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name