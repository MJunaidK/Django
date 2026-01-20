from django.db import models

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.amount} on {self.date}"
