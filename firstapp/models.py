from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=10,unique=True)
    name= models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price=models.FloatField()
    stock_qty=models.IntegerField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sku}-{self.name}"

