
from django.urls import path
from .views import product,category
urlpatterns = [
    path("product/",product,name="product"),
    path("category/",category,name="category")
  
]

