from django.db import models

# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    content = models.TextField(max_length=220)
    price = models.IntegerField(default=0)

