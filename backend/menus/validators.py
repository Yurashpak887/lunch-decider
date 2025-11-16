from datetime import date
from rest_framework.exceptions import ValidationError
from .models import Vote


def validate_menu_is_today(menu):
    if menu.date != date.today():
        raise ValidationError("Можна голосувати тільки за меню на сьогодні")


def validate_employee_not_voted_today(employee):
    if Vote.objects.filter(employee=employee, menu__date=date.today()).exists():
        raise ValidationError("Ви вже проголосували сьогодні")