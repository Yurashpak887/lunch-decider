from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employees.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path("api/auth/login/", CustomTokenObtainPairView.as_view()),
    path("api/auth/refresh/", TokenRefreshView.as_view()),

    # Employees
    path("api/employees/", include("employees.urls")),

    # Restaurants
    path("api/restaurants/", include("restaurants.urls")),

    # Menus
    path("api/menus/", include("menus.urls")),

]
