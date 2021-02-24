from Reminders.models import Reminder
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import timedelta


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ['pk', 'title', 'schedule']


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
