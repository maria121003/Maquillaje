from rest_framework import viewsets, permissions
from .models import Brand, Product_type, Brand_owner, Owner_type
from .serializer import BrandSerializer, Product_typeSerializer, Brand_ownerSerializer, Owner_typeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]        

class Product_typeViewSet(viewsets.ModelViewSet):
    queryset = Product_type.objects.all()
    serializer_class = Product_typeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class Brand_ownerViewSet(viewsets.ModelViewSet):
    queryset = Brand_owner.objects.all()
    serializer_class = Brand_ownerSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class Owner_typeViewSet(viewsets.ModelViewSet):
    queryset = Owner_type.objects.all()  
    serializer_class = Owner_typeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
