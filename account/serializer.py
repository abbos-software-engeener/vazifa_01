from rest_framework import serializers
from .models import Usser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Usser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            "first_name": {
                'required': True
            },
            "last_name": {
                'required': True
            }
        }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=7, max_length=50, error_messages={
            "min_length": _("Parol kamida 7 ta belgidan iborat bo'lishi lozim."),
            "max_length": _("Parol ko'pi bilan 50 ta belgidan iborat bo'lishi mumkin.")
        })
    confirm_password = serializers.CharField(required=True, min_length=7, max_length=50, error_messages={
            "min_length": _("Parol kamida 7 ta belgidan iborat bo'lishi lozim."),
            "max_length": _("Parol ko'pi bilan 50 ta belgidan iborat bo'lishi mumkin.")
        })

    def validate(self, data):
        errors = {}
        if not self.context['request'].user.check_password(data.get('old_password')):
            errors['old_password'] = _("Parol noto'g'ri kiritilgan.")

        if data.get('new_password') != data.get('confirm_password'):
            errors['confirm_password'] = _("Parollar bir xil bo'lishi shart.")

        if data.get('new_password') == data.get('old_password'):
            errors['new_password'] = _("Parol hozirgi parol bilan bir xil.")

        if errors:
            raise serializers.ValidationError(errors)

        return data
