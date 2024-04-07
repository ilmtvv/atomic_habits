import datetime

from rest_framework.exceptions import ValidationError

from habits.models import Habit


def validate_reward_or_related_habit(reward, related_habit):
    if reward and related_habit:
        raise ValidationError("Reward cannot be set if a related habit is specified.")


def validate_time_limit(time_to_complete):
    time_obj = datetime.datetime.strptime(time_to_complete, '%H:%M:%S').time()
    seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    if seconds > 120:
        raise ValidationError("Time limit should not exceed 120 seconds.")


def validate_related_habit(pk_related_habit):
    if pk_related_habit and not Habit.objects.filter(pk=pk_related_habit, nice_habit=True).exists():
        raise ValidationError("Related habit must be pleasurable.")


def validate_pleasurable_habit(nice_habit, related_habit, reward):
    if nice_habit and (related_habit or reward):
        raise ValidationError("Pleasurable habits cannot have rewards or related habits.")


def validate_frequency(periodicity):
    if periodicity > 7:
        raise ValidationError("Habit frequency should not be less than 7 days.")
