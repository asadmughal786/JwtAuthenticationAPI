
from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.UserRegisterationView.as_view(), name='user registeration'),
    path('login/',views.UserLoginView.as_view(), name='user login'),
    path('profile/',views.UserProfileView.as_view(), name='User Profile'),
    path('changepassword/',views.UserChangePasswordView.as_view(), name='Change Password'),
    path('send-password-reset-email/',views.SendPasswordResetEmailView.as_view(),name='reset password email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset-password'),
]
