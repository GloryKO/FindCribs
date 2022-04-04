import email
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from rest_framework import response
from rest_framework.response import Response
from rest_framework import generics,permissions
#from django.http import HttpResponse, JsonResponse
from rest_framework import status
from users.serializers import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.http import HttpResponsePermanentRedirect
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from  .utils import Utils
from . models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
import os
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly

from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from .adapter import GoogleOAuth2AdapterIdToken # import custom adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterIdToken
    #client_class = OAuth2Client

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes=[IsOwnerOrReadOnly,]
