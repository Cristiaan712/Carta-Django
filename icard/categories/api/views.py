from rest_framework.viewsets import ModelViewSet
#Muestra registros a lo logeados
from rest_framework.permissions import IsAuthenticatedOrReadOnly  
from categories.models import Category
from categories.api.serializers import CategorySerializer

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()