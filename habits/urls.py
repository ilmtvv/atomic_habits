from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet

router = DefaultRouter()
router.register(r'', HabitViewSet,)

app_name = HabitsConfig.name

urlpatterns = [

] + router.urls
