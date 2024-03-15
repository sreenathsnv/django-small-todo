from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique= True,)
    # avatar = models.ImageField(upload_to=)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
    

class Todo(models.Model):

    heading = models.TextField(max_length = 30)        
    content = models.TextField()
    done = models.BooleanField(default= False)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)  
    created = models.DateTimeField(auto_now_add = True)

