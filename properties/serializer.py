from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Category, Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields ='__all__'