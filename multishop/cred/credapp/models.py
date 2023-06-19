from django.db import models

# Create your models here.

class categoryDB(models.Model):
    category_name = models.CharField(max_length=100,null=True,blank=True)
    category_image = models.ImageField(upload_to="Category",null=True,blank=True)
    category_description = models.CharField(max_length=1000,null=True,blank=True)

class poductDB(models.Model):
    product_category = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100,null=True,blank=True)
    product_price = models.CharField(max_length=100,null=True,blank=True)
    product_description = models.CharField(max_length=1000,null=True,blank=True)
    product_brand = models.CharField(max_length=100,null=True,blank=True)
    product_image = models.ImageField(upload_to="product-img",null=True,blank=True)






