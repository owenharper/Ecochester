from django.db import models
from django.contrib.auth.models import User
from Item.models import Item
# Create your models here.


class trades(models.Model):
    item1=models.ForeignKey(Item,on_delete=models.CASCADE, related_name='item1')
    item2=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='item2')