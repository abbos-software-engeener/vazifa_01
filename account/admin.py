from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usser


@admin.register(Usser)
class UserModel(UserAdmin):
    pass

