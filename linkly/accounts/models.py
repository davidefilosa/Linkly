from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=225)
    max_num_link = models.IntegerField()

    def __str__(self):
        return self.name



class User(AbstractUser):
    plan = models.ForeignKey(Plan, related_name='user', on_delete=models.CASCADE, default=1)
    
