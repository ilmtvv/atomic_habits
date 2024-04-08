import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, CrontabSchedule


def create_celery_beat_task(data):

    time_parts = data['start_time'].split(":")

    hour, minute, seconds = map(int, time_parts)

    cron_schedule = CrontabSchedule(hour=hour, minute=minute, day_of_week=f'*/{data["periodicity"]}')
    cron_schedule.save()

    task = PeriodicTask.objects.create(
        name=data['id'],
        task='proj_ah.tasks.telegram_notifications',
        args=json.dumps([data['id']]),
        expires=datetime.utcnow() + timedelta(seconds=120),

        crontab=cron_schedule
    )
