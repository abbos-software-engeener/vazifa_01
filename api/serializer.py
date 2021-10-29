from rest_framework import serializers
from .models import *


class AboutStudentS(serializers.ModelSerializer):
    class Meta:
        model = AboutStudent
        fields = '__all__'


class StudentS(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LanguagesS(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class Otm_turiS(serializers.ModelSerializer):
    class Meta:
        model = Otm_turi
        fields = '__all__'


class OtmS(serializers.ModelSerializer):
        class Meta:
            model = Otm
            fields = '__all__'


class AchievementS(serializers.ModelSerializer):
    class Meta:
        model =Achievement
        fields = '__all__'


class ScientificAchievement(serializers.ModelSerializer):
    class Meta:
        model = ScientificAchievement
        fields = '__all__'


class TanlovMAlumotlariS(serializers.ModelSerializer):
    class Meta:
        model = TanlovMAlumotlari
        fields = '__all__'



