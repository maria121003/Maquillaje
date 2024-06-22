from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)

class Product_type(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    varieties = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Brand_owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    nationality = models.CharField(max_length=255, null=True, blank=True)

class Owner_type(models.Model):
    brand_owner = models.ForeignKey(Brand_owner, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE) 

