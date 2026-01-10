from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
