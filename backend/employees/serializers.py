from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ["id", "username", "password", "build_version"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Employee(**validated_data)
        user.set_password(password)
        user.save()
        return user
