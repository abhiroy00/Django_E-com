# models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_bio = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='product_images/')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name
