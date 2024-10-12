from django.contrib.auth.models import User
from django.db import models


def create_path_for_save_avatar(instance: 'Profile', filename: str) -> str:

    """

    Функция для генерации 'path' в корневой папке директории для хранения 'avatar' пользователя

    """

    return 'avatars/user_{pk}/{filename}'.format(pk=instance.pk, filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
