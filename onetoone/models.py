from django.db import models
from django.utils import timezone

<<<<<<< HEAD

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    work_experience = models.SmallIntegerField(default=0)
=======
class User(models.Model):
    name = models.CharField(max_length=20)
    
class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    
>>>>>>> 8b136b7fb9e245aaf262c57113926f69d776ed7e
