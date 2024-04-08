
from rest_framework import viewsets, permissions

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated,
                                  IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = Habit.objects.filter(is_public=True).order_by('id')
        return queryset
