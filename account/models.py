from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        user = Usser(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, **kwargs):
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_staff', False)

        return self._create_user(**kwargs)

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        if not kwargs.get('is_superuser') or not kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_superuser=True and is_staff=True.')

        return self._create_user(**kwargs)


class Usser(AbstractUser):
    objects = UserManager()

    class Meta:
        verbose_name = ("Foydalanuvchi")
        verbose_name_plural = ("Foydalanuvchilar")



