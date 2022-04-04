from django.urls import path
from .views import *

urlpatterns = [
 path('',ListPropertyView.as_view(),name='view-properties'),
 #path('view-create/',propertylist,name='view-create-property'),
 path('view-categories/',CategoriesListView.as_view(),name='categories-list'),
 path('create-property/',CreatePropertyView.as_view(),name='create-property'),
 path('property-detail/<int:pk>/',PropertyDetailView.as_view(),name='property-detail'),
 path('add-favourite/<int:id>/',add_favourite,name='add-to-favourite')
]
