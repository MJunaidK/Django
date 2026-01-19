from django.conf import settings
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='posts/%Y/%m/%d')
   caption = models.TextField(blank=True)
   title = models.CharField(max_length=255)
   slug = models.SlugField(max_length=255, blank=True) 
   created = models.DateTimeField(auto_now_add=True)
   liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True) 
   
def __str__(self):
        return self.title

def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=150, blank=True)

    class Meta:  
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'         
