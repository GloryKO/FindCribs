from django.shortcuts import get_object_or_404
from . models import Category, Property
from rest_framework.response import Response
from .serializer import PropertySerializer,CategorySerializer
from rest_framework.generics import ListAPIView,CreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from .permissions import IsOwnerOrReadOnly
from users.models import CustomUser
from rest_framework.decorators import api_view,permission_classes

class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes=[IsAuthenticated,]


class ListPropertyView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    

    
class CreatePropertyView(CreateAPIView):
    queryset =Property.objects.all()
    serializer_class = PropertySerializer

    

class PropertyDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Property.objects.all()
    serializer_class= PropertySerializer
    permission_classes =[IsOwnerOrReadOnly,]
        


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_favourite(request,id):
    property = get_object_or_404(Property,id=id)
    if property.favourites.filter(id = request.user.id).exists():
        property.favourites.remove(request.user)
        #print("removed")
    else:
        property.favourites.add(request.user)
        #print("added")
    return Response({"Message":"Property added to favourites"})
