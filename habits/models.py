import datetime

from django.db import models

from user.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', null=True, blank=True,)
    place = models.CharField(max_length=11, verbose_name='place',)
    start_time = models.TimeField(verbose_name='start time')
    action = models.CharField(max_length=22, verbose_name='action',)
    nice_habit = models.BooleanField(default=False, verbose_name='nice_habit',)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,)
    periodicity = models.PositiveIntegerField(default=1,)
    reward = models.CharField(max_length=33, null=True, blank=True,)
    time_to_complete = models.DurationField(db_comment='ISO 8601 PT?S', default=datetime.timedelta(seconds=120))
    is_public = models.BooleanField(default=False,)

    def __str__(self):
        return f'{self.user} will be {self.action} at {self.start_time} at {self.place}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
