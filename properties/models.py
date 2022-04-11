from email.policy import default
from logging import PlaceHolder
from django.db import models
from django.forms import ImageField
from users.models import CustomUser, Profile
# Create your models here.
from cloudinary.models import CloudinaryField

CHOICES =(
    ("Terrace", "Terrace"),
    ("Duplex", "Duplex"),
    ("Apartments", "Apartments"),
    ("Land", "Land"),
    ("Hotels", "Hotels"),
    ("Estate Market","Estate Market"),
    #model fixed
    
)
class Category(models.Model):
    name= models.CharField(max_length=250,choices=CHOICES)

    def __str__(self):
        return self.name

PROPERTY_CHOICES =(
    ("Rent", "Rent"),
    ("Sale", "Sale"),
    
)

class Property(models.Model):
    name=models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=250)
    size = models.PositiveIntegerField()
    image1 = models.ImageField(null=False, blank=False, upload_to='images/')
    image2 = models.ImageField(null=False, blank=False, upload_to='images/')
    image3 = models.ImageField(null=False, blank=False, upload_to='images/')
    description =models.TextField()
    property_type =models.CharField(max_length=250,choices=PROPERTY_CHOICES)
    favourites = models.ManyToManyField(CustomUser,related_name='favourite',default=None,blank=True)

    def __str__(self):
        return self.name
