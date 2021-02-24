from Reminders.serializers import ReminderSerializer, UserRegistrationSerializer
from Reminders.models import Reminder
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class ReminderAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request, pk=None):
        if pk is not None:
            try:
                reminder = Reminder.objects.get(id=pk, owner=request.user)
            except Reminder.DoesNotExist:
                return Response({'Message': 'No reminder found!'}, status=status.HTTP_404_NOT_FOUND)
            serialized = ReminderSerializer(reminder)
            return Response(serialized.data)
        reminder = Reminder.objects.filter(owner=request.user)
        serialized = ReminderSerializer(reminder, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = ReminderSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(owner=request.user)
            return Response({'Message': 'Reminder created!'}, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            reminder = Reminder.objects.get(id=pk, owner=request.user)
        except Reminder.DoesNotExist:
            return Response({'Message': 'No reminder found!'}, status=status.HTTP_404_NOT_FOUND)
        serialized = ReminderSerializer(reminder, data=request.data)
        if serialized.is_valid():
            serialized.save(owner=request.user)
            return Response({'Message': 'Data updated completely!'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            reminder = Reminder.objects.get(id=pk, owner=request.user)
        except Reminder.DoesNotExist:
            return Response({'Message': 'No reminder found!'}, status=status.HTTP_404_NOT_FOUND)
        serialized = ReminderSerializer(reminder, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save(owner=request.user)
            return Response({'Message': 'Data updated completely!'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            reminder = Reminder.objects.get(id=pk, owner=request.user)
        except Reminder.DoesNotExist:
            return Response({'Message': 'No reminder found!'}, status=status.HTTP_404_NOT_FOUND)
        reminder.delete()
        return Response({'Message': 'Article deleted!'}, status=status.HTTP_204_NO_CONTENT)


class NotificationAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        reminder = Reminder.objects.filter(owner=request.user, schedule__gte=datetime.now(),
                                           schedule__lte=datetime.now()+timedelta(minutes=10))
        serialized = ReminderSerializer(reminder, many=True)
        return Response(serialized.data)


class UserAPI(APIView):

    def post(self, request):
        serialized = UserRegistrationSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.data['username'],
                serialized.data['email'],
                serialized.data['password']
            )
            return Response({'Message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
