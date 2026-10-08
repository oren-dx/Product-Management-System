from django.db import models
from django.contrib.auth.models import AbstractUser

class ProductUserModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(null=True)

    def __str__(self):
        return f'{self.username}'
    
class ProductModel(models.Model):
    CATEGORY_TYPES =[
        ('Vegetable','Vegetable'),
        ('Fishes','Fishes'),
        ('Fruits','Fruits'),
    ]
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_TYPES,max_length=20,null=True)
    image = models.ImageField(upload_to='media/product',null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2,null=True)
    qty = models.PositiveIntegerField(null=True)
    total_amount = models.FloatField(null=True)
    production_date = models.DateField(null=True)
    created_by = models.ForeignKey(
        ProductUserModel,
        on_delete=models.CASCADE,
        related_name='products',
        null=True)

    def __str__(self):
        return f'{self.name}'




