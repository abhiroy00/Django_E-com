from rest_framework import serializers
from .models import Product, Category

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    # Nested category data (optional)
    product_category = CategorySerializer(read_only=True)
    product_category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='product_category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'product_price',
            'product_bio',
            'product_image',
            'product_category',
            'product_category_id',
            'product_createdAt',
        ]
