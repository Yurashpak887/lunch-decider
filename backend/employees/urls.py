from django.urls import path
from .views import EmployeeCreateView

urlpatterns = [
    path("register/", EmployeeCreateView.as_view()),
]
