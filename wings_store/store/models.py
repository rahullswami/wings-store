from django.db import models

# Create your models here.

class Products(models.Model):
    products_id = models.AutoField
    products_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    products_desc = models.TextField()
    products_image = models.ImageField(upload_to='products')

    def __str__(self) -> str:
        return self.products_name
    
class Contect(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    selecter = models.CharField(max_length=10)
    address = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.fullname