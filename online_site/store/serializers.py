from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'category', 'price', 'have', 'image',
                  'video', 'created_date']
