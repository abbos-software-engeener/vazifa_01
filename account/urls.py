from django.conf.urls.static import static
from django.urls import path

from TalimVAzirligi import settings
from .views import ProfileView, LoginView, MeView, ChangePasswordView, RegisterView

app_name = "account"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path("me/", MeView.as_view(), name="me"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)