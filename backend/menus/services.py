from .models import Menu, Vote
from .validators import validate_menu_is_today, validate_employee_not_voted_today
from datetime import date

def create_vote(employee, menu):
    validate_menu_is_today(menu)
    validate_employee_not_voted_today(employee)
    return Vote.objects.create(employee=employee, menu=menu)


def get_today_results():
    today = date.today()
    menus = Menu.objects.filter(date=today).select_related('restaurant')
    return [
        {
            "restaurant": menu.restaurant.name,
            "votes": Vote.objects.filter(menu=menu).count()
        }
        for menu in menus
    ]