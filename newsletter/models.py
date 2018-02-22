from django.db import models

# Create your models here.


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email

