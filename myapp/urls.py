from django.urls import path
from django.contrib import admin



from myapp import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetails.as_view()),

    path('order/',views.OrderList.as_view()),
    path('order/<int:order_id>',views.OrderDetails.as_view()),

    path('customers/<int:customer_id>/orders/',views.CustomerOrderList.as_view()),
    path('customers/<int:customer_id>/orders/product/<int:product_id>',views.CustomerOrderList.as_view()),


    path('customer/',views.CustomerList.as_view()),
    path('customer/<int:id>/',views.CustomerDetail.as_view()),



]

