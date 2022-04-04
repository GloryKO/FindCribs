from django import views
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from dj_rest_auth.registration.views import VerifyEmailView


urlpatterns =[
    #path('register/', RegisterView.as_view(), name='register'),
    #path('verify-email/',VerifyEmail.as_view(),name="email-verify" ),
    #path('login/',login,name='login'),
     #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         #path('password-reset/<uidb64>/<token>/',
         #PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    #path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         #name='password-reset-complete'),
    path('dj-rest-auth/facebook/',FacebookLogin.as_view(),name='facebook'),
    path('dj-rest-auth/google/', GoogleLoginView.as_view(),name='google'),
    path('view-profile/<int:pk>/',UserProfileView.as_view(),name='view-profile'),
    
    #path('logout/',LogoutAPIView.as_view(),name="logout")
   
]