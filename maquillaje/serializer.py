from rest_framework import serializers
from .models import Brand, Product_type, Brand_owner, Owner_type
from django.conf import settings

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class Product_typeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Product_type
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        product_type = super().create(validated_data)
        if image:
            product_type.image_url = self.save_image(product_type, image)
            product_type.save()
        return product_type

    def save_image(self, product_type, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(product_type.id) + '_' + image.
        name), ContentFile(image.read()))
        return settings.MEDIA_URL + path        

class Brand_ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand_owner
        fields = '__all__'

class Owner_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner_type
        fields = '__all__'                    