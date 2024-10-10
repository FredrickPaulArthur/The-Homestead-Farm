from django.urls import path
from .views import HomeView, RegisterView, ProfileView, Logout

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeForm
from django.contrib.auth.views import PasswordResetCompleteView, PasswordChangeDoneView,  PasswordResetConfirmView, PasswordResetDoneView
from django.contrib.auth.views import auth_login, auth_logout







urlpatterns = [
    path("", HomeView, name="home"),
    path("home/", HomeView, name="home"),
    path("profile/", ProfileView, name="profile"),
    path("register/", RegisterView, name="register"),

    path("login/",
         LoginView.as_view(template_name="registration/login.html"),
         name="login"),

    path("logout/",
         Logout,
         name="logout"),

     ############### Use Django rest framework ###############

     path("password-reset/",
         PasswordResetView.as_view(template_name="password_reset.html"),
         name="password_reset"),

     path("password-reset/done/",
          PasswordResetDoneView.as_view(template_name=""),
          name="password_reset_done"),
     
     path("password-reset-confirm/<uidb64>/<token>/",
          PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
          name="password_reset_confirm"),

     path("password-reset-complete/",
          PasswordResetCompleteView.as_view(template_name=""),
          name="password_reset_complete"),
]