from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 
from django.utils import timezone
from .manager import ItemManager

# Create your models here.
class Item(models.Model):

    class Meta: 
        indexes = [
            models.Index(fields=['item_name', 'item_price']), 
        ]
    def __str__(self):
        return self.item_name 
    
    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.pk})

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, db_index=True)
    item_desc = models.CharField(max_length=500)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    item_image = models.URLField(max_length=300,default='')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    is_deleted = models.BooleanField(default=False) # save delete flag
    deleated_at = models.DateTimeField(null=True, blank=True) # time of deletion

    objects = ItemManager()
    all_objects = models.Manager() # default manager

class Category(models.Model):

    def __str__(self):
        return self.name 

    name = models.CharField(max_length=200)
    added_on = models.DateTimeField(default=timezone.now)
    