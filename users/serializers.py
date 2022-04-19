
from django.db import transaction
from .models import CustomUser, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework import  serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['first_name','last_name','email','phone']




class CustomRegisterSerializer(RegisterSerializer):
    username =None
    first_name =serializers.CharField()
    last_name =serializers.CharField()
    phone = serializers.CharField()



    @transaction.atomic
    def save(self , request):
        user = super().save(request)
        user.email = self.data.get('email')
        user.first_name =self.data.get('first_name')
        user.last_name =self.data.get('last_name')
        user.phone =self.data.get('phone')
        user.save()
      
        return user

class CustomLoginSerializer(LoginSerializer):
    username = None
    

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['fullname','business_name','about','profile_image',]




    