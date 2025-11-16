from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer, VoteSerializer
from .services import create_vote, get_today_results
from datetime import date


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodayMenuView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(date=date.today())


class VoteView(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        employee = self.request.user
        menu = serializer.validated_data['menu']
        vote = create_vote(employee, menu) # це з services.py
        serializer.instance = vote


class TodayResultsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        results = get_today_results()  # це з services.py
        return Response(results)