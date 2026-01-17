from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
class Order(models.Model):
  items = models.CharField(max_length=5000)
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(max_length=20)
  order_date = models.DateTimeField(auto_now_add=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  
  def __str__(self):
        return f"Order {self.name}"    