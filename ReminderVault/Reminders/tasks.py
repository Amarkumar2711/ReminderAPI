from celery import shared_task
from .models import Reminder
from datetime import datetime, timedelta


@shared_task
def send_reminder():
    src = datetime.now()
    curr_time = datetime(src.year, src.month, src.day, src.hour, src.minute, 0)
    reminders_set = Reminder.objects.filter(schedule__gte=curr_time, schedule__lt=curr_time+timedelta(minutes=1))
    for reminder in reminders_set:
        print('Sending ' + reminder.title + ' reminder to ' + reminder.owner.email)
