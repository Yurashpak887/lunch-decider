from .models import Employee


def create_employee(validated_data):
    build_version = validated_data.pop('build_version', '1.0')
    employee = Employee(**validated_data)
    employee.set_password(validated_data['password'])
    employee.build_version = build_version
    employee.save()
    return employee


def update_build_version(employee, build_version):
    employee.build_version = build_version
    employee.save()
    return employee