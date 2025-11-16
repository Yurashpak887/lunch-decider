from rest_framework import serializers
from .models import Menu, Vote


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"



class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "menu", "created_at"]
        read_only_fields = ["created_at"]