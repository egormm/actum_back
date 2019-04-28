from rest_framework import serializers
from .models import Employee, Events, Challenge, Team


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'description')


class RatingEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'rating', 'points_per_day')


class RatingTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'rating', 'points_per_day', 'mult')
