from django.http import JsonResponse
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Product view (GET and POST)
@api_view(["GET", "POST"])
def product(request):
    if request.method == "GET":
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def category(request):
    if request.method == "GET":
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
