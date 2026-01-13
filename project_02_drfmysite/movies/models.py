from django.db import models

# Create your models here.
class MovieData(models.Model):
    title = models.CharField(max_length=100)
    duration = models.FloatField()  
    rating = models.FloatField()
    typ = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True, default='movie_images/default.jpg')

    def __str__(self):
        return self.title
