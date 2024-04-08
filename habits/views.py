
from rest_framework import viewsets, permissions, status

from config.utils import create_celery_beat_task
from habits.models import Habit
from habits.paginations import CustomPagination
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer
from rest_framework.response import Response


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        create_celery_beat_task(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)