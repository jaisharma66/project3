from django.db import models

# Create your models here.

class Topping(models.Model):
    toppings = models.CharField(max_length = 32)

class Regular_Pizza(models.Model):
    type_pizza = models.CharField(max_length = 16)
    small = models.DecimalField(decimal_places=2,max_digits=4)
    large = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Sicilian_Pizza(models.Model):
    type_pizza = models.CharField(max_length = 16)
    small = models.DecimalField(decimal_places=2,max_digits=4)
    large = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Subs(models.Model):
    type_subs = models.CharField(max_length = 64)
    small = models.DecimalField(null=True,decimal_places=2,max_digits=4)
    large = models.DecimalField(decimal_places=2,max_digits=4)
    small_cheese = models.DecimalField(null=True,decimal_places=2,max_digits=4)
    large_cheese = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Pasta(models.Model):
    type_pasta = models.CharField(max_length = 32)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Salads(models.Model):
    type_salad = models.CharField(max_length = 32)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Dinner_Platters(models.Model):
    type_dinner_platters = models.CharField(max_length = 32)
    small = models.DecimalField(decimal_places=2,max_digits=4)
    large = models.DecimalField(decimal_places=2,max_digits=4)
    topping = models.IntegerField()

class Orders(models.Model):
    user = models.CharField(max_length = 64)
    order_items = models.CharField(max_length = 1024)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    topping = models.IntegerField()
    toppings = models.CharField(null=True,blank=True,max_length = 1024)

class Orders_Confirmed(models.Model):
    user = models.CharField(max_length = 64)
    order_items = models.CharField(max_length = 1024)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    topping = models.IntegerField()
    toppings = models.CharField(null=True,blank=True,max_length = 1024)