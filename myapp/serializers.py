from itertools import product

from rest_framework import serializers
from .models import Customer, Product, Order


#edw ftiaxnw ola ta transitions apo python se JSON structures

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True,many=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('products','customer')
