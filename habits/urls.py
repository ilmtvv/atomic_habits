from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitListAPIView

router = DefaultRouter()
router.register(r'', HabitViewSet,)

app_name = HabitsConfig.name

urlpatterns = [
    path('public/', PublicHabitListAPIView.as_view(), name='habits-public-list'),

] + router.urls
