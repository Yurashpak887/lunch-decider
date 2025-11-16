import pytest
from employees.services import create_employee, update_build_version
from employees.models import Employee


@pytest.mark.django_db
def test_create_employee_with_build_version():
    data = {
        'username': 'john',
        'password': 'john123',
        'build_version': '2.1'
    }
    employee = create_employee(data)
    assert employee.username == 'john'
    assert employee.check_password('john123')
    assert employee.build_version == '2.1'


@pytest.mark.django_db
def test_update_build_version():
    employee = Employee.objects.create_user(username='test', password='pass')
    updated = update_build_version(employee, '3.0')
    assert updated.build_version == '3.0'
    assert Employee.objects.get(username='test').build_version == '3.0'