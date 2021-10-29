from rest_framework.decorators import permission_classes
from rest_framework.permissions import *
from .serializer import *
from rest_framework.generics import *
from .permissions import *


class AboutStudentView(ListCreateAPIView):
    queryset = AboutStudent.objects.all()
    serializer_class = AboutStudentS
    permission_classes = [IsAuthenticated, ]


class AboutStudentsView(RetrieveUpdateDestroyAPIView):
    queryset = AboutStudent.objects.all()
    serializer_class = AboutStudentS
    permission_classes = [IsAdminUser, IsAdmin]


class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentS
    permission_classes = [IsAuthenticated]


class StudentsView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentS
    permission_classes = [IsAdminUser, IsAdmin,]


class LanguageView(ListCreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesS
    permission_classes = [IsAuthenticated,]


class LanguagesView(RetrieveUpdateDestroyAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesS
    permission_classes = [IsAdminUser, IsAdmin,]


class OtmView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Otm.objects.all()
    serializer_class = OtmS
    permission_classes = [IsAdmin]


class Otm_turiView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Otm.objects.all()
    serializer_class = Otm_turiS
    permission_classes = [IsAdmin]


class AchievementView(ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementS
    permission_classes = [IsAuthenticated, ]


class AchievementsView(RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementS
    permission_classes = [IsAdminUser|IsAdmin]
