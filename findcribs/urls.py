"""findcribs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework.schemas import get_schema_view
#from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from dj_rest_auth.views import  LogoutView
from dj_rest_auth.registration.views import VerifyEmailView,ConfirmEmailView
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

schema_view = get_schema_view( 
   openapi.Info(
      title="FindCribs API",
      default_version='v1',
      description="The API for FindCribs App",
      terms_of_service="https://www.google.com/policies/terms/",
      #contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,]
)
urlpatterns = [
    
    #path('api/users/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   
   path(
        'dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ), # Needs to be defined before the registration path

    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    #path('dj-rest-auth/logout/',LogoutView.as_view()),
    path('properties/',include('properties.urls')),

    path('api/v1/doc/', csrf_exempt(schema_view.with_ui('swagger', cache_timeout=0), )),
    path('redoc/', csrf_exempt(schema_view.with_ui('redoc', cache_timeout=0))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)