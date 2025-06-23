from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

#signup


class SignupInfo(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100, null=False, blank=False)
    subcategory = models.CharField(max_length=100, null=False, blank=False)

    # Define a default manager for Product objects
    objects = models.Manager()

    def __str__(self):
        return self.name

class Cart(models.Model):
    # model is related to a single user, and if that user is deleted, also delete all instances
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()

    def get_total(self):
        total = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitem_set')
    quantity = models.PositiveIntegerField(default=1)

    objects = models.Manager()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.name
