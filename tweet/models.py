from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class tweet(models.Model):

    name= models.CharField(max_length=14)
    body= models.CharField(max_length=140)
    Image= CloudinaryField()
    like_count= models.IntegerField(max_length=11)
    created_at= models.DateTimeField()
    updated_at= models.DateTimeField()