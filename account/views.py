from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Usser
from .serializer import LoginSerializer, UserSerializer, ProfileSerializer, ChangePasswordSerializer,RegisterSerializer
from api.responses import ResponseFail, ResponseSuccess
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import password_changed


class RegisterView(generics.CreateAPIView):
    queryset = Usser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(APIView):
    permission_classes = [~IsAuthenticated]

    def post(self, request):
        serializers = LoginSerializer(data=request.data)
        if not serializers.is_valid():
            return ResponseFail(serializers.errors)

        user = authenticate(username=serializers.validated_data["username"],
                            password=serializers.validated_data["password"])

        if user is None:
            return ResponseFail({
                "password": _("Login va/yoki parol noto'g'ri")
            })

        refresh = RefreshToken.for_user(user)

        return ResponseSuccess({
            "token": str(refresh.access_token),
            "user": UserSerializer(user).data
        })


class MeView(APIView):
    """
    Foydalanuvchi haqida ma'lumot qaytaradi
    """
    def get(self, request):
        return ResponseSuccess({
            "user": UserSerializer(request.user).data
        })


class ProfileView(APIView):
    """
    Foydalanuvchi ma'lumotlarini tahrirlaydi
    """
    def post(self, request):
        profile = ProfileSerializer(instance=request.user, data=request.data)
        if not profile.is_valid():
            return ResponseFail(profile.errors)

        profile.save()

        return ResponseSuccess({
            "user": profile.data
        })


class ChangePasswordView(APIView):
    """
    Foydalanuvchini parolni o'zgartiradi
    """
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return ResponseFail(serializer.errors)

        user.set_password(serializer.validated_data.get("new_password"))
        user.save()

        password_changed(serializer.validated_data['new_password'], request.user)

        return ResponseSuccess()
