import pytest
from django.utils import timezone
from datetime import date, timedelta
from menus.services import create_vote, get_today_results
from menus.models import Menu, Vote
from rest_framework.exceptions import ValidationError
from employees.models import Employee


@pytest.mark.django_db
class TestCreateVote:
    def test_create_vote_success(self, employee, menu_today):
        """Успішне створення голосу"""
        vote = create_vote(employee, menu_today)
        assert vote.employee == employee
        assert vote.menu == menu_today
        assert Vote.objects.filter(employee=employee, menu=menu_today).exists()

    def test_cannot_vote_twice_same_day(self, employee, menu_today):
        """Не можна голосувати двічі за день"""
        create_vote(employee, menu_today)
        with pytest.raises(ValidationError, match="Ви вже проголосували сьогодні"):
            create_vote(employee, menu_today)

    def test_cannot_vote_for_yesterday_menu(self, employee, menu_yesterday):
        """Не можна голосувати за вчорашнє меню"""
        with pytest.raises(ValidationError, match="Можна голосувати тільки за меню на сьогодні"):
            create_vote(employee, menu_yesterday)

    def test_cannot_vote_for_tomorrow_menu(self, employee, menu_tomorrow):
        """Не можна голосувати за завтрашнє меню"""
        with pytest.raises(ValidationError, match="Можна голосувати тільки за меню на сьогодні"):
            create_vote(employee, menu_tomorrow)


@pytest.mark.django_db
class TestGetTodayResults:
    def test_returns_empty_list_if_no_menus_today(self):
        """Порожній список, якщо немає меню на сьогодні"""
        results = get_today_results()
        assert results == []

    def test_returns_correct_votes_count(self, employee, menu_today, another_menu_today):
        """Правильно рахує голоси"""
        # Голос від employee
        Vote.objects.create(employee=employee, menu=menu_today)
        # Додатковий голос
        another_employee = Employee.objects.create_user(username="user2", password="pass")
        Vote.objects.create(employee=another_employee, menu=menu_today)

        results = get_today_results()

        assert len(results) == 2
        pizza_result = next(r for r in results if r["restaurant"] == "Pizza Palace")
        assert pizza_result["votes"] == 2

        pasta_result = next(r for r in results if r["restaurant"] == "Pasta House")
        assert pasta_result["votes"] == 0

    def test_ignores_old_votes(self, employee, menu_yesterday):
        """Ігнорує голоси за старі меню"""
        Vote.objects.create(employee=employee, menu=menu_yesterday)
        results = get_today_results()
        assert results == []