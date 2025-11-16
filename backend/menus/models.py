from django.db import models
from restaurants.models import Restaurant
from employees.models import Employee

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()  # можна зберігати JSON або текст

    class Meta:
        unique_together = ("restaurant", "date")

    def __str__(self):
        return f"{self.restaurant.name} — {self.date}"

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "menu")

    def __str__(self):
        return f"{self.employee.username} → {self.menu}"
