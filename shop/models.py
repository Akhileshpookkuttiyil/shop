from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_category', args=[self.slug])
    
class Seller(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    class Meta:
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.name
    
class Colour(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)   
    class Meta:
        verbose_name_plural = 'colours'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='products/')
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    color = models.ForeignKey(Colour,related_name='product_color', on_delete=models.CASCADE)
    description = models.TextField()
    ratings = models.CharField(max_length=8)
    seller = models.ForeignKey(Seller, related_name='product_seller', on_delete=models.CASCADE)
    price = models.IntegerField()
    is_new = models.BooleanField(default=True)
    offer = models.IntegerField()
    stock = models.IntegerField()
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def total_price(self):
        return self.price - (self.price * (self.offer / 100))

    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug]) 
