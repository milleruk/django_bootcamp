from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    # id = models.AutoField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_CASCADE) # delete everything associated with user ever created
    title = models.CharField(max_length=220)
    content = models.TextField(max_length=220)
    price = models.IntegerField(default=0)

