from django.db import models
from shop.models import *

# Create your models here.
class Cartlist(models.Model):
    cart_id=models.CharField(max_length=255,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    cart_id=models.ForeignKey(Cartlist,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.product


    def get_amount(self):
        total=self.product.total_price()
        return total*self.quantity
