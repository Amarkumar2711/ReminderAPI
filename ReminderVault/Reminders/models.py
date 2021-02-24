from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Reminder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=30)
    schedule = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
