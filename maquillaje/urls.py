from django.urls import include, path
from rest_framework import routers
from .views import BrandViewSet, Product_typeViewSet, Brand_ownerViewSet, Owner_typeViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'product_types', Product_typeViewSet)
router.register(r'brand_owners', Brand_ownerViewSet)
router.register(r'owner_types', Owner_typeViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]