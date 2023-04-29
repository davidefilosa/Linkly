from django.db import models
from accounts.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, related_name='links', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    decription = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, related_name="links", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name