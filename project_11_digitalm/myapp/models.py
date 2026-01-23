from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name 
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"Order of {self.product.name} by {self.email}"    