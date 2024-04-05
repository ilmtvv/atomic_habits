from rest_framework import serializers

from habits.models import Habit


class RelatedHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    related_habit = RelatedHabitSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
