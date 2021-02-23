from django.db import models
from django.contrib.auth.models import User
from trade_search.models import Hub
# Create your models here.
class Item(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner', null=True)
    itemid = models.AutoField(primary_key=True)
    itemname=models.TextField()
    description=models.TextField()
    created_at=models.DateField()
    image=models.ImageField()
    country_code=models.TextField(blank=True)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE,null=True)