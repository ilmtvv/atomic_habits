
from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class HabitTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(email='test@case.com')
        self.user.set_password('qwe123RTY456')

        self.access_token = str(RefreshToken.for_user(self.user).access_token)

        self.client.force_authenticate(user=self.user, token=self.access_token)

        # self.habit = Habit.objects.create(
        #     place="test",
        #     start_time="22:00",
        #     action="jump",
        #     reward="win",
        # )

    def test_get_habit_list(self):
        responce = self.client.get(
            reverse('habits:habit-list')
        )

        # print(responce.status_code)
        # print(responce.json())

        self.assertEqual(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_habit_create(self):
        habit = {
            'place': "test",
            'start_time': "22:00",
            'action': "jump",
            'reward': "win",
        }

        responce = self.client.post(
            reverse('habits:habit-list'),
            habit
        )

        # print(responce.status_code)
        # print(responce.json())

        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_create_validation(self):
        habit = {
            'place': "test",
            'start_time': "22:00",
            'action': "jump",
            'reward': "win",
            'related_habit': 1,
        }

        responce = self.client.post(
            reverse('habits:habit-list'),
            habit
        )

        # print(responce.status_code)
        # print(responce.json())

        self.assertEqual(
            responce.status_code,
            status.HTTP_400_BAD_REQUEST
        )
