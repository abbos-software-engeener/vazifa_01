from .views import *
from django.urls import path

app_name = 'api'


urlpatterns = [
    path('aboutstudent/',AboutStudentView.as_view()),
    path('aboutstudent/<int:pk>/',AboutStudentsView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<int:pk>/',StudentsView.as_view()),
    path('languages/', LanguageView.as_view()),
    path('languages/<int:pk>/',LanguagesView.as_view()),
    path('otm/',OtmView.as_view()),
    path('otm/<int:pk>/',OtmView.as_view()),
    path('otm_turi/<int:pk>/',Otm_turiView.as_view()),
    path('achievement/',AchievementView.as_view()),
    path('achievement/<int:pk>/',AchievementsView.as_view()),



]
