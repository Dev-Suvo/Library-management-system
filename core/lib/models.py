from django.db import models

# Create your models here.

class Lbook(models.Model):
    b_name = models.CharField(max_length=100)
    b_des = models.TextField()
    b_image = models.ImageField(upload_to="books")


    