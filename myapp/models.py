from symtable import Class

from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.description}"+" "+f"{self.product_name}"+" "+f"{self.price}"



    def __str__(self):
        return f"{self.payment_method}"+" "+f"{self.amount}"


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    ### created a superuser with email: kaps.j.8@gmail.com username:jkapsalis password: jkapsalis

class Order(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Payment(models.Model):
    amount =models.DecimalField(max_digits=10,decimal_places=2)
    payment_method =models.CharField(max_length=100)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
