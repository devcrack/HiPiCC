from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.contrib.auth.hashers import check_password


class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

