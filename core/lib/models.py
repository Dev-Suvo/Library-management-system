from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    b_name = models.CharField(max_length=100)
    b_des = models.TextField()
    b_image = models.ImageField(upload_to="books")


    