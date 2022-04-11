from dataclasses import field
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import Category, Property
from users.serializers import ProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields =['name',]

class PropertySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    owner = ProfileSerializer()
    class Meta:
        model = Property
        fields = '__all__'
