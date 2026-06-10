from django.urls import path
from . import views 

app_name = "accounts"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile2/', views.ProfileGenericView.as_view(), name='profile2'),
    
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', views.RequestResetPasswordView.as_view(), name='reset-password'),
    path('reset-password/confirm/', views.SetNewPasswordView.as_view(), name='reset-password-confirm'),
    ]
