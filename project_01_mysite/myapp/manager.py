from django.db import models

# class ItemManager(models.Manager):
    # def cheap_items(self):
        # return self.filter(item_price__lt=5)
    # def expensive_items(self):
        # return self.filter(item_price__gte=5)
    # def search(self, keyword):
        # return self.filter(item_name__icontains=keyword)

class ItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False) 
    
    def deleted_items(self):
        return super().get_queryset().filter(is_deleted=True)