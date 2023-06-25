from django.db import models

# Create your models here.

class house(models.Model):
    name=models.CharField(max_length=50,default="")
    room =models.CharField(max_length=50,default="")
    kitchen =models.CharField(max_length=50,default="")
    bathroom =models.CharField(max_length=50,default="")
    drawing_room =models.CharField(max_length=50,default="")
    images = models.ImageField(upload_to="pics",max_length=50,default="")
    def __str__(self):
        return self.name
