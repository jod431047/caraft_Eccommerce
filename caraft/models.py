from django.contrib.auth.models import User
from django.db import models


class Caraft(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='caraft')
    
    def __str__(self):
        return self.name