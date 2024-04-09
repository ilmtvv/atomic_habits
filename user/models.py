from django.contrib.auth.models import AbstractUser
from django.db import models

null_blank = {'null': True, 'blank': True}


class User(AbstractUser):
    username = models.CharField(max_length=25, default='user')
    email = models.EmailField(unique=True)
    telegram = models.CharField(max_length=33, **null_blank)

    # user_pk = models.IntegerField(**null_blank)
    user_pk = models.ForeignKey('self', on_delete=models.SET_NULL, **null_blank)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.telegram

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
