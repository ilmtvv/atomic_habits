import datetime

from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):

        if data.get('reward') and data.get('related_habit'):
            raise serializers.ValidationError("Cannot specify both reward and related habit.")

        if data.get('time_to_complete'):
            threshold = datetime.timedelta(seconds=120)

            if data['time_to_complete'] > threshold:
                raise serializers.ValidationError("Execution time cannot exceed 120 seconds.")

        if data.get('related_habit') and not data['related_habit'].nice_habit:
            raise serializers.ValidationError("Related habit must be pleasurable.")

        if data.get('nice_habit') and (data.get('reward') or data.get('related_habit')):
            raise serializers.ValidationError("Pleasurable habit cannot have reward or related habit.")

        if data.get('periodicity') and data['periodicity'] < 7:
            raise serializers.ValidationError("Habit frequency cannot be less than 7 days.")

        return data
