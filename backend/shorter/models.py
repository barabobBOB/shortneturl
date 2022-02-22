from django.db import models
from django.contrib.auth.models import AbstractUser

class Createuser(models.Model):
    username = models.CharField(max_length=20)
    password = models.TextField()
    email = models.EmailField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

class User(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Createuser, on_delete=models.CASCADE, null=True)
    
"""class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_user = models.ForeignKey(Createuser, on_delete=models.CASCADE)"""