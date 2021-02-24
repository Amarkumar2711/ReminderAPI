# Generated by Django 3.0.3 on 2021-02-23 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminders', '0004_auto_20210220_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='reminder_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_active',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_date',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_finished',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_time',
        ),
        migrations.AddField(
            model_name='reminder',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 15, 51, 14, 986718)),
        ),
    ]
