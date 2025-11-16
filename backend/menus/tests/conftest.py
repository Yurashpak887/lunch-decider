import pytest
from employees.models import Employee
from restaurants.models import Restaurant
from menus.models import Menu
from datetime import date, timedelta


@pytest.fixture
def employee():
    return Employee.objects.create_user(username='testuser', password='testpass123')


@pytest.fixture
def another_employee():
    return Employee.objects.create_user(username='user2', password='testpass123')


@pytest.fixture
def restaurant(employee):
    return Restaurant.objects.create(name="Pizza Palace", owner=employee)


@pytest.fixture
def another_restaurant(employee):
    return Restaurant.objects.create(name="Pasta House", owner=employee)


@pytest.fixture
def menu_today(restaurant):
    return Menu.objects.create(
        restaurant=restaurant,
        date=date.today(),
        items="Pizza, Salad"
    )


@pytest.fixture
def another_menu_today(another_restaurant):
    return Menu.objects.create(
        restaurant=another_restaurant,
        date=date.today(),
        items="Pasta, Bread"
    )


@pytest.fixture
def menu_yesterday(restaurant):
    return Menu.objects.create(
        restaurant=restaurant,
        date=date.today() - timedelta(days=1),
        items="Old Menu"
    )


@pytest.fixture
def menu_tomorrow(restaurant):
    return Menu.objects.create(
        restaurant=restaurant,
        date=date.today() + timedelta(days=1),
        items="Future Menu"
    )