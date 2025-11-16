from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Employee
from .serializers import EmployeeSerializer
from .services import create_employee, update_build_version


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        build_version = request.headers.get('X-Build-Version', '1.0')
        mutable_data = request.data.copy()
        mutable_data['build_version'] = build_version

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        employee = create_employee(serializer.validated_data)
        serializer.instance = employee

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        build_version = self.context['request'].headers.get('X-Build-Version', '1.0')
        update_build_version(self.user, build_version)
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer