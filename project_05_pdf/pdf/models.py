from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15) 
    summary = models.TextField(blank=True)
    degree = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.name
