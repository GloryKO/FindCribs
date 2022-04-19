from dataclasses import field
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import Category, Property
from users.serializers import ProfileSerializer,UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields =['name',]

class PropertyListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    #owner = ProfileSerializer()
    class Meta:
        model = Property
        exclude =['favourites','owner']

class CreatePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields =['name','category','price','location','size','image1',
            'image2','image3','description','property_type',]        


class PropertyDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    owner = UserSerializer()
    class Meta:
        model = Property
        exclude =['favourites']