
from rest_framework import viewsets

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.validators import validate_reward_or_related_habit, validate_time_limit, validate_related_habit, \
    validate_pleasurable_habit, validate_frequency


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        validate_reward_or_related_habit(serializer.data['reward'], serializer.data['related_habit'])
        validate_time_limit(serializer.data['time_to_complete'])
        validate_related_habit(serializer.data['related_habit'])
        validate_pleasurable_habit(serializer.data['nice_habit'], serializer.data['related_habit'], serializer.data['reward'])
        validate_frequency(serializer.data['periodicity'])
