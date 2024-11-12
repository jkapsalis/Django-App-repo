from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer


class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    def get(self, request, *args, **kwargs):
        customer_id = kwargs['id']
        queryset = Customer.objects.filter(pk=customer_id)
        if queryset.exists():
            customer_object = queryset[0]
            serializer = CustomerSerializer(customer_object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        customer_id = kwargs['id']
        queryset = Customer.objects.filter(pk=customer_id)
        if queryset.exists():
             customerobject = queryset[0]
             serializer = CustomerSerializer(customerobject,data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data,status=status.HTTP_200_OK)
             else:
                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):
    def get(self,request,*args,**kwargs):
        product_id = kwargs['id']
        queryset = Product.objects.filter(pk=product_id)
        if queryset.exists():
            product_object = queryset[0]
            serializer = ProductSerializer(product_object)
            return Response(serializer.data,status=status.HTTP_200_OK)


class OrderList(APIView):
    def get(self,request,format=None):
        order = Order.objects.all()
        serializer= OrderSerializer(order,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetails(APIView):
    def get(self, request, *args, **kwargs):
        order_id = kwargs['id']
        queryset = Order.objects.filter(pk=order_id)
        if queryset.exists():
            order_object = queryset[0]
            serializer = OrderSerializer(order_object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request,*args,**kwargs):
        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,*args,**kwargs):
        order_id = kwargs['id']
        queryset = Order.objects.filter(pk=order_id)
        if queryset.exists():
             order_object = queryset[0]
             serializer = OrderSerializer(order_object,data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data,status=status.HTTP_200_OK)
             else:
                 return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerOrderList(APIView):
    def get(self, request, *args, **kwargs):
        customer_id = kwargs['customer_id']
        product_id = kwargs['product_id']
        queryset = Order.objects.filter(customer_id=customer_id,products__id=product_id)
        serializer = OrderSerializer(queryset,  many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class PaymentList(APIView):
    def post(self, request, *args, **kwargs):
        order_id = kwargs['order_id']
        data=request.data
        data['order_id']=order_id
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
