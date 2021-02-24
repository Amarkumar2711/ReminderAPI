from django.contrib import admin
from Reminders.models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'title', 'schedule']
