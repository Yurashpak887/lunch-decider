from django.urls import path
from .views import (
    MenuCreateView, TodayMenuView,
    VoteView, TodayResultsView
)

urlpatterns = [
    path("create/", MenuCreateView.as_view()),
    path("today/", TodayMenuView.as_view()),
    path("vote/", VoteView.as_view()),
    path("results/", TodayResultsView.as_view()),
]
