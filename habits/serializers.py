from rest_framework import serializers

from habits.models import Habit


class UserSerializer(serializers.ModelSerializer):
    related_habit = serializers.SerializerMethodField()

    @staticmethod
    def get_related_habit(obj):
        if obj.related_habit is not None:
            pk = obj.related_habit.pk
            return obj.get(pk=pk)

    class Meta:
        model = Habit
        fields = '__all__'
