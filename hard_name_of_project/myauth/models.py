from django.db import models
from django.contrib.auth.models import User


def profile_avatar_directory_path(instance: 'Profile', filename: str) -> str:

     """

     Функция для генерации 'path' в корневой папке директории для хранения 'avatar' пользователя

     """

     return 'avatars/user_{pk}/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
     avatar = models.ImageField(null=True, blank=True, upload_to=profile_avatar_directory_path)
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     bio = models.TextField(max_length=500, blank=True)
     agreement_accepted = models.BooleanField(default=False)
