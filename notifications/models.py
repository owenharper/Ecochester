from django.db import models
from django.contrib.auth.models import User
from Item.models import Item
# Create your models here.


class notifications(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='wishlist')