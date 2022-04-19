from tokenize import blank_re
from django.db import models

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length=250,blank=False,)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    fullname= models.CharField(max_length=500)
    business_name = models.CharField(max_length=250)
    #phone = models.CharField(max_length=250,)
    about =models.TextField()
    profile_image = CloudinaryField('image',blank=True)



    def __str__(self):
        return self.fullname


  
    



